"""
URL configuration for luanvan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from django.contrib import admin
# from Data_Interaction.admin import admin_site
from django.urls import path

from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from django.urls import re_path,path


from django.views.generic.base import TemplateView
from django.conf.urls.static import serve

from django.views.generic import RedirectView

from django.contrib.auth import views as auth_views

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

from .views.admin.login_admin import *
from .views.admin.product_admin import *
from .views.admin.image_content_admin import *
from .views.admin.image_slider_admin import *

from sleekweb.sitemaps import *
from django.contrib.sitemaps.views import sitemap

sitemaps_dict = {
    'static': StaticViewSitemap,
    'product': detail_product_Sitemap,
}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps_dict}, name='sitemap'),


    path('account/login', login_client,name='login_client'),

    path('', tab_best_sellers_client,name='tab_best_sellers_client'),
    path('products-home', tab_products_client,name='tab_products_client'),
    path('regimens-home', tab_regimens_client,name='tab_regimens_client'),
    

    path('blog', nav_blog_client,name='nav_blog_client'),
    path('mineral-research', nav_nghien_cuu_lam_san,name='nav_nghien_cuu_lam_san'),
    path('products', nav_products_client,name='nav_products_client'),

    path('north-partner', select_kvmb_client,name='select_kvmb_client'),
    path('southern-partner', select_kvmn_client,name='select_kvmn_client'),

    path('blog-1', blog_1_client,name='blog_1_client'),
    path('blog-2', blog_2_client,name='blog_2_client'),
    path('blog-3', blog_3_client,name='blog_3_client'),

    path('about-us', about_ve_chung_toi_client,name='about_ve_chung_toi_client'),
    path('news-awards', about_tin_tuc_giai_thuong_client,name='about_tin_tuc_giai_thuong_client'),
    path('vision-mission', about_tam_nhin_va_su_menh_client,name='about_tam_nhin_va_su_menh_client'),
    path('contact', about_lien_he_client,name='about_lien_he_client'),

    path('contact', about_lien_he_client,name='about_lien_he_client'),

    path('scientific-research', link_nghien_cuu_khoa_hoc_client,name='link_nghien_cuu_khoa_hoc_client'),
    path('clinical-results', link_ket_qua_lam_san_client,name='link_ket_qua_lam_san_client'),

    path('detail-proudct/<int:pk>/', detail_product_client,name='detail_product_client'),

    path('admin/login', login_admin,name='login_admin'),
    path('admin/logout', logout_admin,name='logout_admin'),
    path('admin/product', product_admin,name='product_admin'),
    path('admin/product/add', product_add_admin,name='product_add_admin'),
    path('admin/product/edit/<int:pk>/', product_edit_admin,name='product_edit_admin'),
    path('admin/product/remove', product_remove_admin,name='product_remove_admin'),

    path('admin/product/size/add', size_product_add_admin,name='size_product_add_admin'),
    path('admin/product/size/remove',size_product_remove_admin,name='size_product_remove_admin'),

    path('admin/image-content',image_content_admin,name='image_content_admin'),
    path('admin/image-slider',image_slider_admin,name='image_slider_admin'),


    path('signup-email',signup_email_client,name='signup_email_client'),

]