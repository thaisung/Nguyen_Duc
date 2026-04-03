from django.http import HttpResponse
from django.template.loader import render_to_string

# myapp/middleware.py

from django.shortcuts import redirect
import datetime
from django.http import HttpResponse

from django.http import HttpResponse, HttpResponsePermanentRedirect

class BlockAfterDateMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Thiết lập ngày hết hạn
        self.expiry_date = datetime.datetime(2025, 5, 5)

    def __call__(self, request):
        current_time = datetime.datetime.now()

        if current_time > self.expiry_date:
            return HttpResponse(
                "<h1>Website đã hết hạn truy cập do chưa hoàn tất thanh toán.</h1><p>Vui lòng liên hệ người đã tạo ra mã nguồn.</p>",
                content_type="text/html; charset=utf-8", 
                status=403
            )

        response = self.get_response(request)
        return response

# Mapping URL cũ → URL mới (chỉ phần path, không có domain)
REDIRECT_MAP = {
    '/hydrinity-hyacyn-active-mist-xit-phuc-hoi-khang-khuan-lam-diu-da-sau-treatment.html':
        '/hydrinity-hyacyn-active-mist-xit-khoang-hocl-lam-diu-can-bang-da.html',

    '/encore-body-hydrator-kem-duong-am-toan-than.html':
        '/hydrinity-encore-body-hydrator-kem-duong-am-toan-than-duy-tri-do-am.html',

    '/hydrinity-restorative-ha-serum-tinh-chat-phuc-hoi-da.html':
        '/hydrinity-restorative-ha-serum-tinh-chat-cham-soc-da-chuyen-sau.html',

    '/hydrinity-retaxome-daily-retinal-hydrator-kem-duong-da-ho-tro-duong-am-giup-da-trong-sang-va-min-mang-hon.html':
        '/hydrinity-retaxome-daily-retinal-hydrator-kem-duong-da-cang-min-san-chac.html',

    '/hydrinity-hydri-c-daily-vitamin-c-moisturizer-kem-duong-vitamin-c-tan-trong-dau-cap-am-sang-da.html':
        '/hydrinity-hydri-c-daily-vitamin-c-moisturizer-kem-duong-vitamin-c-cap-am-sang-da.html',

    # mới
    '/detail-proudct/hydrinity-renewing-ha-serum-tinh-chat-tre-hoa-tai-tao-da/':
        '/hydrinity-renewing-ha-serum-tinh-chat-cham-soc-da-chuyen-sau.html',

    '/detail-proudct/hydrinity-vivid-brightening-serum-serum-lam-sang-da-mo-nam-sau-treatment/':
        '/hydrinity-vivid-brightening-serum-tinh-chat-cham-soc-da-tuoi-sang.html',

    '/detail-proudct/hydrinity-hyacyn-active-mist-xit-phuc-hoi-khang-khuan-lam-diu-da-sau-treatment/':
        '/hydrinity-hyacyn-active-mist-xit-khoang-hocl-lam-diu-can-bang-da.html',

    '/detail-proudct/hydrinity-restorative-ha-serum-tinh-chat-phuc-hoi-da/':
        '/hydrinity-restorative-ha-serum-tinh-chat-cham-soc-da-chuyen-sau.html',

    '/detail-proudct/encore-body-hydrator-kem-duong-am-toan-than/':
        '/hydrinity-encore-body-hydrator-kem-duong-am-toan-than-duy-tri-do-am.html',

    '/detail-proudct/hydrinity-eye-renew-complex-kem-mat-tre-hoa-giam-quang-tham/':
        '/hydrinity-eye-renew-complex-kem-duong-cham-soc-vung-da-mat.html',

    '/detail-proudct/hydrinity-prelude-facial-cleanser-sua-rua-mat-lam-sach-sau-diu-nhe-cho-da-nhay-cam/':
        '/hydrinity-prelude-facial-treatment-cleanser-sua-rua-mat-diu-nhe-duy-tri-do-am.html',

    '/detail-proudct/hydrinity-luxe-lip-hydrator-duong-moi-cang-mong-phuc-hoi-sau-lieu-trinh/':
        '/hydrinity-luxe-lip-hydrator-son-duong-cap-am-moi-mem-mai.html',

    '/detail-proudct/hydrinity-hydri-c-kem-duong-vitamin-c-kep-lam-sang-cap-am-cho-da-nhay-cam/':
        '/hydrinity-hydri-c-daily-vitamin-c-moisturizer-kem-duong-vitamin-c-cap-am-sang-da.html',

    '/detail-proudct/hydrinity-retaxome-daily-retinal-hydrator-kem-duong-da-ho-tro-duong-am-giup-da-trong-sang-va-min-mang-hon/':
        '/hydrinity-retaxome-daily-retinal-hydrator-kem-duong-da-cang-min-san-chac.html',
}

REDIRECT_MAP_410 = [
    '/detail-proudct/hydrinity-restorative-ha-masque-mat-na-phuc-hoi-da-voi-ha-thuy-phan-biocellulose-vo-trung/',
    '/blog-1',
    '/blog-2',
    '/blog-3'
]
    

class Redirect404ToHomeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code == 404:
            path = request.path

            # 1. Kiểm tra mapping cố định trước
            if path in REDIRECT_MAP:
                return HttpResponsePermanentRedirect(REDIRECT_MAP[path])

            # 2. Xử lý /blog/ → /{slug}.html
            if path.startswith('/blog/'):
                slug = path[len('/blog/'):].rstrip('/')
                return HttpResponsePermanentRedirect(f'/{slug}.html')

            if path in REDIRECT_MAP_410:
                html = render_to_string('sleekweb/410.html')
                return HttpResponse(html, status=410)

            # 3. Render trang 404 tuỳ chỉnh
            html = render_to_string('sleekweb/404.html')
            return HttpResponse(html, status=404)

        return response


class MaintenanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Cho phép truy cập nếu là trang login
        if request.path.startswith('/admin/login'):
            return self.get_response(request)

        # Cho phép nếu user đã đăng nhập và username là "bdmin"
        if request.user.is_authenticated and request.user.username == 'bdmin':
            return self.get_response(request)

        # Còn lại trả về trang bảo trì
        html = render_to_string('sleekweb/maintenance.html')
        return HttpResponse(html, status=503)
