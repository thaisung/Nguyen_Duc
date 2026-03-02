from django.http import HttpResponse

def robots_txt(request):
    return HttpResponse(
        "User-agent: *\n"
        "Allow: /\n\n"
        "Sitemap: https://hydrinity.com.vn/sitemap.xml",
        content_type="text/plain"
    )