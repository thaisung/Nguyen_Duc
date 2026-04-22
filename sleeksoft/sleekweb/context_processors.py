from .models import Website


def site_info(request):
    """Injects Website singleton into every template context as `site_obj`."""
    try:
        site_obj = Website.objects.filter(Count=1).first() or Website.objects.first()
    except Exception:
        site_obj = None
    return {'site_obj': site_obj}
