# blog/sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import *

from datetime import datetime

from .views.client.login_client import *

from .views.client.home_client import *
from .views.client.tab_best_sellers_client import *
from .views.client.tab_products_client import *
from .views.client.tab_regimens_client import *

from .views.client.nav_blog_client import *
from .views.client.nav_nghien_cuu_lam_san import *
from .views.client.nav_products_client import *

from .views.client.select_kvmb_client import *
from .views.client.select_kvmn_client import *


from .views.client.blog_1_client import *
from .views.client.blog_2_client import *
from .views.client.blog_3_client import *

from .views.client.about_ve_chung_toi_client import *
from .views.client.about_tin_tuc_giai_thuong_client import *
from .views.client.about_tam_nhin_va_su_menh_client import *
from .views.client.about_lien_he_client import *

from .views.client.link_ket_qua_lam_san_client import *
from .views.client.link_nghien_cuu_khoa_hoc_client import *
from .views.client.detail_product_client import *
from .views.client.signup_email_client import *

protocol = 'https'

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return [
            'tab_best_sellers_client',
            'tab_products_client',
            'tab_regimens_client',
            'nav_blog_client',
            'nav_nghien_cuu_lam_san',
            'nav_products_client',
            'select_kvmb_client',
            'select_kvmn_client',
            'blog_1_client',
            'blog_2_client',
            'blog_3_client',
            'about_ve_chung_toi_client',
            'about_tin_tuc_giai_thuong_client',
            'about_tam_nhin_va_su_menh_client',
            'about_lien_he_client',
            'link_nghien_cuu_khoa_hoc_client',
            'link_ket_qua_lam_san_client',
        ]

    def location(self, item):
        return reverse(item)
    
class detail_product_Sitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9
    protocol = protocol

    def items(self):
        # Lấy tất cả các Category_product từ cơ sở dữ liệu
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.Update_time

    def location(self, item):
        # Dùng slug của mỗi category_product để tạo đường dẫn
        return reverse('detail_product_client', kwargs={'pk': item.id})

# class detail_sound_Sitemap(Sitemap):
#     changefreq = "weekly"
#     priority = 0.9
#     protocol = 'https'

#     def items(self):
#         return Sound_List.objects.all()

#     def lastmod(self, obj):
#         return obj.created_at_sound
    
#     def location(self, obj):
#         return reverse('detail_sound', args=[obj.sound_url])
    
# class detail_video_Sitemap(Sitemap):
#     changefreq = "weekly"
#     priority = 0.9
#     protocol = 'https'

#     def items(self):
#         return Video_List.objects.all()

#     def lastmod(self, obj):
#         return obj.created_at_video
    
#     def location(self, obj):
#         return reverse('detail_video', args=[obj.video_url])
    
# class image_video_Sitemap(Sitemap):
#     changefreq = "weekly"
#     priority = 0.9
#     protocol = 'https'

#     def items(self):
#         return Video_List.objects.all()

#     def lastmod(self, obj):
#         return obj.created_at_video
    
#     def location(self, obj):
#         image_path = obj.video_Image.url
#         return image_path
    
# class StaticSitemap1(Sitemap):
#     changefreq = "monthly"
#     priority = 0.5
#     protocol = 'https'
 
#     def items(self):
#         return ['about','copyright','contact'] 
    
#     def lastmod(self, obj):

#         return None
 
#     def location(self, item):
#         return reverse(item)
    

