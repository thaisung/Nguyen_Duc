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
from .views.client.api_client import *

from .views.admin.login_admin import *
from .views.admin.product_admin import *
from .views.admin.image_content_admin import *
from .views.admin.image_slider_admin import *
from .views.admin.change_website_admin import *
from .views.admin.change_ncls_admin import *
from .views.admin.change_vct_admin import *
from .views.admin.change_tnsm_admin import *
from .views.admin.change_ttgt_admin import *
from .views.admin.change_lh_admin import *
from .views.admin.change_dsdt_admin import *
from .views.admin.change_nckh_admin import *
from .views.admin.change_kqls_admin import *
from .views.admin.change_kqls1_admin import *
from .views.admin.change_blog_admin import *
from .views.admin.change_kqls_post_admin import *
from .views.admin.user_admin import *

from sleekweb.sitemaps import *
from django.contrib.sitemaps.views import sitemap

sitemaps_dict = {
    'static': StaticViewSitemap,
    'product': detail_product_Sitemap,
}

urlpatterns = [

    # path('admin/', admin.site.urls),

    #api
    path('add-mb', add_dsdt_mb,name='add_dsdt_mb'),
    path('add-mn', add_dsdt_mn,name='add_dsdt_mn'),
    #endapi
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps_dict}, name='sitemap'),


    path('account/login', login_client,name='login_client'),

    path('', tab_best_sellers_client,name='tab_best_sellers_client'),
    path('products-home', tab_products_client,name='tab_products_client'),
    path('regimens-home', tab_regimens_client,name='tab_regimens_client'),
    

    path('blog', nav_blog_client,name='nav_blog_client'),
    path('blog/<str:slug>', nav_blog_detail_client,name='nav_blog_detail_client'),
    path('mineral-research', nav_nghien_cuu_lam_san,name='nav_nghien_cuu_lam_san'),
    path('products', nav_products_client,name='nav_products_client'),

    path('north-partner', select_kvmb_client,name='select_kvmb_client'),
    path('southern-partner', select_kvmn_client,name='select_kvmn_client'),

    path('blog-1', blog_1_client,name='blog_1_client'),
    path('blog-2', blog_2_client,name='blog_2_client'),
    path('blog-3', blog_3_client,name='blog_3_client'),

    path('about-us', about_ve_chung_toi_client,name='about_ve_chung_toi_client'),
    path('news-awards', about_tin_tuc_giai_thuong_client,name='about_tin_tuc_giai_thuong_client'),
    path('news-awards/<str:slug>/',about_tin_tuc_giai_thuong_detail_client,name='about_tin_tuc_giai_thuong_detail_client'),
    path('news-awards/cultivating-confidence-the-hydrinity-way-to-a-luxurious-skin-journey', link_tt_gt_1_client,name='link_tt_gt_1_client'),
    path('news-awards/hydrinity-accelerated-skin-science-expands-into-the-united-kingdom-and-ireland', link_tt_gt_2_client,name='link_tt_gt_2_client'),
    path('vision-mission', about_tam_nhin_va_su_menh_client,name='about_tam_nhin_va_su_menh_client'),
    path('contact', about_lien_he_client,name='about_lien_he_client'),

    path('contact', about_lien_he_client,name='about_lien_he_client'),

    path('scientific-research', link_nghien_cuu_khoa_hoc_client,name='link_nghien_cuu_khoa_hoc_client'),
    path('clinical-results', link_ket_qua_lam_san_client,name='link_ket_qua_lam_san_client'),

    path('detail-proudct/<str:slug>/', detail_product_client,name='detail_product_client'),

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
    path('admin/image-slider-remove',image_slider_remove_admin,name='image_slider_remove_admin'),
    path('admin/image-slider-order',image_slider_order_admin,name='image_slider_order_admin'),

    path('admin/change-website',change_website_admin,name='change_website_admin'),
    path('admin/change-home',change_home_admin,name='change_home_admin'),
    path('admin/change-ncls',change_ncls_admin,name='change_ncls_admin'),
    path('admin/change-vct',change_vct_admin,name='change_vct_admin'),
    path('admin/change-vct1',change_vct1_admin,name='change_vct1_admin'),
    path('admin/order-change-vct1',change_vct1_order_admin,name='change_vct1_order_admin'),
    path('admin/change-tnsm',change_tnsm_admin,name='change_tnsm_admin'),
    path('admin/change-tnsm1',change_tnsm1_admin,name='change_tnsm1_admin'),
    path('admin/order-change-tnsm1',change_tnsm1_order_admin,name='change_tnsm1_order_admin'),
    path('admin/change-ttgt',change_ttgt_admin,name='change_ttgt_admin'),
    path('admin/change-ttgt1',change_ttgt1_admin,name='change_ttgt1_admin'),

    path('admin/change-ttgt1/add', change_ttgt1_add_admin, name='change_ttgt1_add_admin'),
    path('admin/change-ttgt1/edit/<int:pk>/', change_ttgt1_edit_admin, name='change_ttgt1_edit_admin'),
    path('admin/change-ttgt1/remove/<int:pk>/', change_ttgt1_remove_admin, name='change_ttgt1_remove_admin'),

    path('admin/order-change-ttgt1',change_ttgt1_order_admin,name='change_ttgt1_order_admin'),
    path('admin/change-lh',change_lh_admin,name='change_lh_admin'),
    path('admin/change-dsdt-mb',change_lh_admin,name='change_lh_admin'),
    path('admin/change-nckh',change_nckh_admin,name='change_nckh_admin'),
    path('admin/change-nckh1',change_nckh1_admin,name='change_nckh1_admin'),
    path('admin/order-change-nckh1',change_nckh1_order_admin,name='change_nckh1_order_admin'),
    path('admin/change-nckh2',change_nckh2_admin,name='change_nckh2_admin'),
    path('admin/order-change-nckh2',change_nckh2_order_admin,name='change_nckh2_order_admin'),
    path('admin/change-kqls',change_kqls_admin,name='change_kqls_admin'),
    path('admin/change-kqls1',change_kqls1_admin,name='change_kqls1_admin'),
    path('admin/change-dsdt',change_dsdt_admin,name='change_dsdt_admin'),
    path('admin/change-dsdt-remove',change_dsdt_remove_admin,name='change_dsdt_remove_admin'),

    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('admin/change-blog', change_blog_admin, name='change_blog_admin'),
    path('admin/change-blog/add', change_blog_add_admin, name='change_blog_add_admin'),
    path('admin/change-blog/edit/<int:pk>/', change_blog_edit_admin, name='change_blog_edit_admin'),
    path('admin/change-blog/remove/<int:pk>/', change_blog_remove_admin, name='change_blog_remove_admin'),

    path('admin/change-kqls-post', change_kqls_post_admin, name='change_kqls_post_admin'),
    path('admin/change-kqls-post/add', change_kqls_post_add_admin, name='change_kqls_post_add_admin'),
    path('admin/change-kqls-post/edit/<int:pk>/', change_kqls_post_edit_admin, name='change_kqls_post_edit_admin'),
    path('admin/change-kqls-post/remove/<int:pk>/', change_kqls_post_remove_admin, name='change_kqls_post_remove_admin'),

    path('admin/user/edit/<int:pk>/', user_edit_admin,name='user_edit_admin'),
    path('admin/user/change-password/', user_change_password_admin,name='user_change_password_admin'),


    path('signup-email',signup_email_client,name='signup_email_client'),

    path('kqls-post/<str:slug>', kqls_post_detail_client,name='kqls_post_detail_client'),

]