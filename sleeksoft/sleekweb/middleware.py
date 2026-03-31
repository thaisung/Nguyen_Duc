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

class Redirect404ToHomeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code == 404:
            path = request.path  # ví dụ: /blog/ten-bai-viet

            # Nếu path bắt đầu bằng /blog/ → redirect sang /ten-bai-viet.html
            if path.startswith('/blog/'):
                slug = path[len('/blog/'):]          # bỏ /blog/
                slug = slug.rstrip('/')              # bỏ trailing slash nếu có
                new_url = f'/{slug}.html'
                return HttpResponsePermanentRedirect(new_url)

            # Render trang 404 tuỳ chỉnh
            html = render_to_string('sleekweb/404.html')
            return HttpResponse(html, status=404)


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
