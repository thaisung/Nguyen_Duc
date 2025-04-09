from django.http import HttpResponse
from django.template.loader import render_to_string

class MaintenanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Cho phép admin truy cập nếu cần
        if request.path.startswith('/admin/'):
            return self.get_response(request)

        html = render_to_string('sleekweb/maintenance.html')
        return HttpResponse(html, status=503)
    
# from django.http import HttpResponse
# from django.template.loader import render_to_string
# from django.contrib.auth import get_user
# from django.utils.deprecation import MiddlewareMixin

# class MaintenanceMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         user = get_user(request)

#         # Cho phép superuser (đã đăng nhập) truy cập mọi nơi
#         if user.is_authenticated and user.is_superuser:
#             return None  # Cho phép request tiếp tục

#         # Còn lại hiển thị trang bảo trì
#         html = render_to_string('sleekweb/maintenance.html')
#         return HttpResponse(html, status=503)