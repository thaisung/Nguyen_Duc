from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
                'Slug',
                'Seo_Title',
                'Seo_Description',
                'Name',
                'Title',
                'Category',
                'Introduce',
                'Describe',
                'Main_ingredients',
                'How_use',
                'Avatar'
                ]
        labels = {
            'Slug': 'Đường dẫn',
            'Seo_Title': 'Tiêu đề SEO',
            'Seo_Description': 'Mô tả SEO',
            'Name': 'Tên sản phẩm',
            'Title': 'Chi tiết',
            'Category': 'Danh mục sản phẩm',
            'Introduce': 'Giới thiệu sản phẩm',
            'Describe': 'Mô tả sản phẩm',
            'Main_ingredients': 'Thành phần chính',
            'How_use': 'Cách sử dụng',
            'Avatar': 'Ảnh đại diện'
        }

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['Slug','Seo_Title','Seo_Description','Title', 'Content','Avatar']
        labels = {
            'Slug': 'Đường dẫn',
            'Seo_Title': 'Tiêu đề SEO',
            'Seo_Description': 'Mô tả SEO',
            'Title': 'Tiêu đề',
            'Content': 'Nội dung bài viết',
            'Avatar': 'Ảnh đại diện'
        }

class ttgt1Form(forms.ModelForm):
    class Meta:
        model = Edit_ttgt1
        fields = ['Slug','Seo_Title','Seo_Description','Title','Category', 'Content','Photo']
        labels = {
            'Slug': 'Đường dẫn',
            'Seo_Title': 'Tiêu đề SEO',
            'Seo_Description': 'Mô tả SEO',
            'Title': 'Tiêu đề',
            'Category':'Danh mục',
            'Content': 'Nội dung bài viết',
            'Photo': 'Ảnh đại diện'
        }

class Edit_kqls1_Form(forms.ModelForm):
    class Meta:
        model = Edit_kqls1
        fields = ['Content']
        labels = {
            'Content': 'Nội dung bài viết',
        }

class KqlsPostForm(forms.ModelForm):
    class Meta:
        model = KqlsPost
        fields = ['Slug','Seo_Title','Seo_Description','Title', 'Content','Avatar']
        labels = {
            'Slug': 'Đường dẫn',
            'Seo_Title': 'Tiêu đề SEO',
            'Seo_Description': 'Mô tả SEO',
            'Title': 'Tiêu đề',
            'Content': 'Nội dung bài viết',
            'Avatar': 'Ảnh đại diện'
        }

