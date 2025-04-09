from django.http import HttpResponse
from django.template.loader import render_to_string

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
