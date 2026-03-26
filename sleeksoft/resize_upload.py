from __future__ import annotations

import argparse
import io
import time
from pathlib import Path

from PIL import Image, ImageOps, UnidentifiedImageError

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compress images recursively in upload folder (including subfolders)."
    )
    parser.add_argument(
        "--path",
        type=str,
        default="upload",
        help="Target folder to scan recursively. Default: upload",
    )
    parser.add_argument(
        "--quality",
        type=int,
        default=82,
        help="Output quality for JPEG/WebP, range 1-95. Default: 82",
    )
    parser.add_argument(
        "--max-width",
        type=int,
        default=1920,
        help="Max width after resize, set 0 to disable. Default: 1920",
    )
    parser.add_argument(
        "--max-height",
        type=int,
        default=1920,
        help="Max height after resize, set 0 to disable. Default: 1920",
    )
    parser.add_argument(
        "--min-size-kb",
        type=int,
        default=200,
        help="Skip files smaller than this (KB). Default: 200",
    )
    parser.add_argument(
        "--include-ext",
        nargs="+",
        default=sorted(SUPPORTED_EXTENSIONS),
        help="Extensions to include. Example: --include-ext .jpg .jpeg .png .webp",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Analyze only, do not overwrite files.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Write optimized file even when it is not smaller.",
    )
    parser.add_argument(
        "--progress-every",
        type=int,
        default=10,
        help="Print progress every N files. Default: 10",
    )
    return parser.parse_args()


def normalize_extensions(ext_list: list[str]) -> set[str]:
    result: set[str] = set()
    for ext in ext_list:
        if not ext:
            continue
        ext = ext.lower()
        if not ext.startswith("."):
            ext = "." + ext
        result.add(ext)
    return result & SUPPORTED_EXTENSIONS


def print_progress(
    index: int,
    total: int,
    stats: dict[str, int],
    start_time: float,
    progress_every: int,
) -> None:
    if progress_every <= 0:
        return
    if index % progress_every != 0 and index != total:
        return

    elapsed = max(time.time() - start_time, 0.001)
    speed = index / elapsed
    percent = (index / total) * 100 if total else 100.0
    saved_mb = (stats["bytes_before"] - stats["bytes_after"]) / (1024 * 1024)
    print(
        f"[PROGRESS] {index}/{total} ({percent:.1f}%) | "
        f"optimized={stats['optimized']} failed={stats['failed']} | "
        f"saved={saved_mb:.2f} MB | {speed:.1f} file/s"
    )


def optimized_payload(path: Path, quality: int, max_width: int, max_height: int) -> bytes | None:
    with Image.open(path) as img:
        img = ImageOps.exif_transpose(img)

        if max_width > 0 and max_height > 0:
            img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)

        suffix = path.suffix.lower()
        format_map = {
            ".jpg": "JPEG",
            ".jpeg": "JPEG",
            ".png": "PNG",
            ".webp": "WEBP",
            ".bmp": "BMP",
            ".tif": "TIFF",
            ".tiff": "TIFF",
        }
        file_format = format_map.get(suffix)
        if not file_format:
            return None

        save_kwargs: dict[str, object] = {}
        if file_format == "JPEG":
            if img.mode in ("RGBA", "LA"):
                alpha = img.getchannel("A")
                background = Image.new("RGB", img.size, (255, 255, 255))
                background.paste(img.convert("RGBA"), mask=alpha)
                img = background
            elif img.mode == "P" or img.mode != "RGB":
                img = img.convert("RGB")
            save_kwargs = {"quality": quality, "optimize": True, "progressive": True}
        elif file_format == "PNG":
            save_kwargs = {"optimize": True, "compress_level": 9}
        elif file_format == "WEBP":
            if img.mode not in ("RGB", "RGBA"):
                img = img.convert("RGBA" if "A" in img.getbands() else "RGB")
            save_kwargs = {"quality": quality, "method": 6}
        elif file_format == "TIFF":
            save_kwargs = {"compression": "tiff_lzw"}

        output = io.BytesIO()
        img.save(output, format=file_format, **save_kwargs)
        return output.getvalue()


def optimize_tree(
    root: Path,
    quality: int,
    max_width: int,
    max_height: int,
    min_size_kb: int,
    include_ext: set[str],
    dry_run: bool,
    force: bool,
    progress_every: int,
) -> dict[str, int]:
    files = [p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in include_ext]
    stats = {
        "files_scanned": len(files),
        "optimized": 0,
        "skipped_small": 0,
        "skipped_not_smaller": 0,
        "failed": 0,
        "bytes_before": 0,
        "bytes_after": 0,
    }
    min_size_bytes = min_size_kb * 1024
    total = len(files)
    start = time.time()

    for index, path in enumerate(files, start=1):
        before = 0
        before_counted = False
        try:
            before = path.stat().st_size
            stats["bytes_before"] += before
            before_counted = True

            if before < min_size_bytes:
                stats["skipped_small"] += 1
                stats["bytes_after"] += before
                print_progress(index, total, stats, start, progress_every)
                continue

            payload = optimized_payload(path, quality, max_width, max_height)
            if payload is None:
                stats["skipped_not_smaller"] += 1
                stats["bytes_after"] += before
                print_progress(index, total, stats, start, progress_every)
                continue

            after = len(payload)
            should_write = force or after < before
            if not should_write:
                stats["skipped_not_smaller"] += 1
                stats["bytes_after"] += before
                print_progress(index, total, stats, start, progress_every)
                continue

            if not dry_run:
                tmp = path.with_name(path.name + ".tmp_optimized")
                tmp.write_bytes(payload)
                tmp.replace(path)

            stats["optimized"] += 1
            stats["bytes_after"] += after
            print_progress(index, total, stats, start, progress_every)

        except (UnidentifiedImageError, OSError, ValueError) as exc:
            stats["failed"] += 1
            current_size = before if before_counted else (path.stat().st_size if path.exists() else 0)
            if not before_counted:
                stats["bytes_before"] += current_size
            stats["bytes_after"] += current_size
            print(f"[FAILED] {path}: {exc}")
            print_progress(index, total, stats, start, progress_every)

    return stats


def main() -> int:
    args = parse_args()
    root = Path(args.path).expanduser().resolve()
    include_ext = normalize_extensions(args.include_ext)

    if not root.exists() or not root.is_dir():
        print(f"[ERROR] Folder does not exist or is not a directory: {root}")
        return 1
    if not 1 <= args.quality <= 95:
        print("[ERROR] --quality must be in range 1-95.")
        return 1
    if args.max_width < 0 or args.max_height < 0:
        print("[ERROR] --max-width and --max-height must be >= 0.")
        return 1
    if not include_ext:
        print("[ERROR] No valid extensions provided in --include-ext.")
        return 1

    stats = optimize_tree(
        root=root,
        quality=args.quality,
        max_width=args.max_width,
        max_height=args.max_height,
        min_size_kb=args.min_size_kb,
        include_ext=include_ext,
        dry_run=bool(args.dry_run),
        force=bool(args.force),
        progress_every=max(1, int(args.progress_every)),
    )

    if stats["files_scanned"] == 0:
        print("[INFO] No matching image files found.")
        return 0

    saved = stats["bytes_before"] - stats["bytes_after"]
    mode = "DRY RUN" if args.dry_run else "WRITE MODE"
    print(f"Completed ({mode})")
    print(f"- Files scanned: {stats['files_scanned']}")
    print(f"- Optimized: {stats['optimized']}")
    print(f"- Skipped (small): {stats['skipped_small']}")
    print(f"- Skipped (not smaller): {stats['skipped_not_smaller']}")
    print(f"- Failed: {stats['failed']}")
    print(f"- Total before: {stats['bytes_before'] / (1024 * 1024):.2f} MB")
    print(f"- Total after: {stats['bytes_after'] / (1024 * 1024):.2f} MB")
    print(f"- Saved: {saved / (1024 * 1024):.2f} MB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
