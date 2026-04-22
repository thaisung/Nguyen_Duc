from django.db import models

# Create your models here.
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin

from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

# Create your models here.

class User(AbstractUser):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Quản lý tài khoản Đăng Nhập"
    AbstractUser._meta.get_field('email').blank = False
    AbstractUser._meta.get_field('email').blank = False
    AbstractUser._meta.get_field('username').blank = False
    AbstractUser._meta.get_field('username').blank = False
    AbstractUser._meta.get_field('password').blank = False
    AbstractUser._meta.get_field('password').blank = False
    
    Avatar = models.ImageField(upload_to='user_image', default="user_image/user_empty.png", null=True,blank=True)
    Full_name = models.CharField('Họ và tên', max_length=255,blank=True, null=True)
    Phone_number = models.CharField('Số điện thoại', max_length=255,blank=True, null=True)
    OTP = models.CharField('Mã Otp',max_length=255, null=True,blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    class Meta:
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['email']),
            models.Index(fields=['Full_name']),
        ]

class Product(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Sản phẩm"
    Seo_Title = models.CharField(max_length=500, blank=True, null=True)
    Seo_Description = models.CharField(max_length=1000, blank=True, null=True)
    Avatar = models.ImageField(upload_to='PRODUCT_AVATAR',null=True,blank=True)
    Name = models.CharField('Tên SP', max_length=500,blank=True, null=True)
    Slug = models.SlugField(unique=True,max_length=350, blank=True, null=True)  # Thêm slug
    Title = models.CharField('Chi tiết SP', max_length=500,blank=True, null=True)
    Category = models.CharField('Danh mục', max_length=250,blank=True, null=True)
    Cosbeauty_link = models.URLField('Link Cosbeauty', max_length=500, blank=True, null=True)
    Price = models.CharField('Giá', max_length=255,blank=True, null=True)
    Introduce = models.TextField('Giới thiệu',blank=True, null=True)
    Describe = RichTextUploadingField(blank=True, null=True)
    Main_ingredients = models.TextField('Thành phần chính',blank=True, null=True)
    How_use = models.TextField('Cách sử dụng',blank=True, null=True)
    # Ingredients_table = models.TextField('Bảng thành phần',blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

    def save(self, *args, **kwargs):
        if self.Slug:
            # Kiểm tra slug người dùng nhập đã chuẩn chưa
            normalized_slug = slugify(self.Slug)
            if self.Slug == normalized_slug:
                base_slug = self.Slug
            else:
                base_slug = normalized_slug
        else:
            # Không nhập slug → lấy theo Name
            base_slug = slugify(self.Name)

        slug = base_slug
        n = 1

        # Đảm bảo slug unique
        while (
            Product.objects.filter(Slug=slug).exclude(pk=self.pk).exists()
            or KqlsPost.objects.filter(Slug=slug).exists()
            or BlogPost.objects.filter(Slug=slug).exists()
        ):
            slug = f"{base_slug}-{n}"
            n += 1

        self.Slug = slug
        super().save(*args, **kwargs)

class Photo(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Ảnh sản phẩm"
    
    Avatar = models.ImageField(upload_to='PRODUCT',null=True,blank=True)
    Belong_Product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='list_photo',blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True) 

class Photo_ncls(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Ảnh sản phẩm NCLS"
    
    Avatar = models.ImageField(upload_to='PRODUCT_NCLS',null=True,blank=True)
    Belong_Product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='list_photo_ncls',blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True) 

class Size(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Size sản phẩm"
    
    Name = models.CharField('Tên Size SP', max_length=500,blank=True, null=True)
    Price = models.CharField('Giá', max_length=255,blank=True, null=True)
    Belong_Product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='list_size',blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

class Email(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Size sản phẩm"
    
    Name = models.CharField('Tên email', max_length=200,blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

class Photo_Content(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Ảnh và Nội dung"
    
    Photo1 = models.ImageField(upload_to='PHOTO_CONTENT',null=True,blank=True)
    Content1 = models.TextField('Nội dung 1',blank=True, null=True)
    Photo2 = models.ImageField(upload_to='PHOTO_CONTENT',null=True,blank=True)
    Content2 = models.TextField('Nội dung 2',blank=True, null=True)
    Photo3 = models.FileField(upload_to='PHOTO_CONTENT',null=True,blank=True)
    Content3 = models.TextField('Nội dung 3',blank=True, null=True)
    Count = models.IntegerField('Số bản ghi',blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

class Photo_Slider(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Ảnh Slider"
    
    Photo = models.ImageField(upload_to='PHOTO_SLIDER',null=True,blank=True)
    Count = models.IntegerField('Số bản ghi',blank=True, null=True)
    Order = models.IntegerField('Thứ tự xuất hiện',blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)


class Website(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Thông tin trang web"
    
    Logo = models.ImageField(upload_to='Change_Website',null=True,blank=True)
    Phone_number = models.CharField('Số điện thoại', max_length=50,blank=True, null=True)
    Text_run = models.CharField('Chữ chạy', max_length=100,blank=True, null=True)
    Email = models.CharField('Email', max_length=50,blank=True, null=True)
    Count = models.IntegerField('Số bản ghi',blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

class Edit_home(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Thay đổi trang chủ"
    
    Title = models.CharField('Tiêu đề', max_length=200,blank=True, null=True)
    Count = models.IntegerField('Số bản ghi',blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

class Edit_ncls(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Thông tin trang ncls"
    
    Nckh = models.ImageField(upload_to='Edit_ncls',null=True,blank=True)
    Kqls = models.ImageField(upload_to='Edit_ncls',null=True,blank=True)
    Count = models.IntegerField('Số bản ghi',blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

class Edit_vct(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Thông tin trang vct"
    
    Title1 = models.CharField('Tiêu đề 1', max_length=200,blank=True, null=True)
    Content1 = models.CharField('Nội dung 1',blank=True, null=True)
    Content2 = models.CharField('Nội dung 2',blank=True, null=True)
    Title2 = models.CharField('Tiêu đề 2', max_length=200,blank=True, null=True)
    Content3 = models.CharField('Nội dung 3',blank=True, null=True)
    Photo1 = models.ImageField(upload_to='Edit_vct',null=True,blank=True)
    Photo2 = models.ImageField(upload_to='Edit_vct',null=True,blank=True)
    Photo3 = models.ImageField(upload_to='Edit_vct',null=True,blank=True)
    Count = models.IntegerField('Số bản ghi',blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

class Edit_vct1(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Thông tin vct phần con"
    
    Title = models.CharField('Tiêu đề', max_length=200,blank=True, null=True)
    Content = models.CharField('Nội dung',blank=True, null=True)
    Photo = models.ImageField(upload_to='Edit_vct',null=True,blank=True)
    Order = models.IntegerField('Thứ tự',blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

class Edit_tnsm(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Thông tin trang tnsm"
    
    Title1 = models.CharField('Tiêu đề 1', max_length=200,blank=True, null=True)
    Content1 = models.CharField('Nội dung 1',blank=True, null=True)
    Photo1 = models.ImageField(upload_to='Edit_tnsm',null=True,blank=True)
    Title2 = models.CharField('Tiêu đề 2', max_length=50,blank=True, null=True)
    Title3 = models.CharField('Tiêu đề 2', max_length=50,blank=True, null=True)
    Content2 = models.CharField('Nội dung 3',blank=True, null=True)
    Photo2 = models.ImageField(upload_to='Edit_tnsm',null=True,blank=True)
    Count = models.IntegerField('Số bản ghi',blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

class Edit_tnsm1(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Thông tin tnsm phần con"
    
    Title = models.CharField('Tiêu đề', max_length=200,blank=True, null=True)
    Content = models.CharField('Nội dung',blank=True, null=True)
    Photo = models.ImageField(upload_to='Edit_tnsm',null=True,blank=True)
    Order = models.IntegerField('Thứ tự',blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

class Edit_ttgt(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Thông tin tin tức, giải thưởng"
    
    Title1 = models.CharField('Tiêu đề', max_length=200,blank=True, null=True)
    Photo1 = models.ImageField(upload_to='Edit_ttgt',null=True,blank=True)
    Count = models.IntegerField('Số bản ghi',blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

class Edit_ttgt1(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Thông tin tin tức, giải thưởng"
    Seo_Title = models.CharField(max_length=500, blank=True, null=True)
    Seo_Description = models.CharField(max_length=1000, blank=True, null=True)
    Title = models.CharField('Tiêu đề', max_length=200,blank=True, null=True)
    Slug = models.SlugField(unique=True,max_length=350, blank=True, null=True)
    Category = models.CharField('Danh mục', max_length=200,blank=True, null=True)
    Content = RichTextUploadingField(blank=True, null=True)
    Photo = models.ImageField(upload_to='Edit_ttgt',null=True,blank=True)
    Order = models.IntegerField('Thứ tự',blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

    def save(self, *args, **kwargs):
        if not self.Slug:
            base_slug = slugify(self.Title)
            slug = base_slug
            n = 1
            # Nếu slug đã tồn tại thì thêm số đuôi
            while Edit_ttgt1.objects.filter(Slug=slug).exists():
                slug = f"{base_slug}-{n}"
                n += 1
            self.Slug = slug
        super().save(*args, **kwargs)

class Edit_lh(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Thông tin map"
    
    Address = models.CharField('Địa chỉ liên hệ', max_length=200,blank=True, null=True)
    Link_map = models.CharField('Link map', max_length=1000,blank=True, null=True)
    Count = models.IntegerField('Số bản ghi',blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

class Edit_dsdt(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Danh sách đối tác"
    
    Name = models.CharField('Tên phòng khám', max_length=200,blank=True, null=True)
    Address = models.CharField('Địa chỉ liên hệ', max_length=200,blank=True, null=True)
    Link = models.CharField('Link', max_length=200,blank=True, null=True)
    Photo = models.ImageField(upload_to='Edit_dsdt',null=True,blank=True)
    Order = models.IntegerField('Thứ tự',blank=True, null=True)
    Category = models.CharField('Danh mục', max_length=200,blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

class Edit_nckh(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Thông tin trang nckh"
    
    Photo1 = models.ImageField(upload_to='Edit_nckh',null=True,blank=True)
    Title1 = models.CharField('Tiêu đề 1', max_length=200,blank=True, null=True)
    Content1 = models.CharField('Nội dung 1',blank=True, null=True)
    Title2 = models.CharField('Tiêu đề 2', max_length=200,blank=True, null=True)
    Photo2 = models.ImageField(upload_to='Edit_tnsm',null=True,blank=True)
    Title3 = models.CharField('Tiêu đề 2', max_length=200,blank=True, null=True)
    Photo3 = models.ImageField(upload_to='Edit_tnsm',null=True,blank=True)
    Content2 = models.CharField('Nội dung 3',blank=True, null=True)
    Count = models.IntegerField('Số bản ghi',blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

class Edit_nckh1(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Thông tin nckh phần con"
    
    Title = models.CharField('Tiêu đề', max_length=200,blank=True, null=True)
    Content = models.CharField('Nội dung',blank=True, null=True)
    Photo = models.ImageField(upload_to='Edit_nckh',null=True,blank=True)
    Order = models.IntegerField('Thứ tự',blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

class Edit_nckh2(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Thông tin nckh phần con"
    
    Title = models.CharField('Tiêu đề', max_length=200,blank=True, null=True)
    Content = models.CharField('Nội dung',blank=True, null=True)
    Photo = models.ImageField(upload_to='Edit_nckh',null=True,blank=True)
    Order = models.IntegerField('Thứ tự',blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

class Edit_kqls(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Thông tin trang kqls"
    
    Photo1 = models.ImageField(upload_to='Edit_kqls',null=True,blank=True)
    Title1 = models.CharField('Tiêu đề 1', max_length=200,blank=True, null=True)
    Content1 = models.CharField('Nội dung 1',blank=True, null=True)
    Title2 = models.CharField('Tiêu đề 2', max_length=50,blank=True, null=True)
    Content2 = models.CharField('Nội dung 3',blank=True, null=True)
    Count = models.IntegerField('Số bản ghi',blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)


class BlogPost(models.Model):
    Seo_Title = models.CharField(max_length=500, blank=True, null=True)
    Seo_Description = models.CharField(max_length=1000, blank=True, null=True)
    Title = models.CharField(max_length=350, blank=True, null=True)
    Slug = models.SlugField(unique=True,max_length=350, blank=True, null=True)  # Thêm slug
    Content = RichTextUploadingField(blank=True, null=True)
    Avatar = models.ImageField(upload_to='AVATAR_BLOG',null=True,blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

    def save(self, *args, **kwargs):
        if self.Slug:
            # Kiểm tra slug người dùng nhập đã chuẩn chưa
            normalized_slug = slugify(self.Slug)
            if self.Slug == normalized_slug:
                base_slug = self.Slug
            else:
                base_slug = normalized_slug
        else:
            # Không nhập slug → lấy theo Name
            base_slug = slugify(self.Title)

        slug = base_slug
        n = 1

        # Đảm bảo slug unique
        while (
            BlogPost.objects.filter(Slug=slug).exclude(pk=self.pk).exists()
            or KqlsPost.objects.filter(Slug=slug).exists()
            or Product.objects.filter(Slug=slug).exists()
        ):
            slug = f"{base_slug}-{n}"
            n += 1

        self.Slug = slug
        super().save(*args, **kwargs)

class Edit_kqls1(models.Model):
    Content = RichTextUploadingField(blank=True, null=True)
    Order = models.IntegerField('Thứ tự',blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

class KqlsPost(models.Model):
    Seo_Title = models.CharField(max_length=500, blank=True, null=True)
    Seo_Description = models.CharField(max_length=1000, blank=True, null=True)
    Title = models.CharField(max_length=350, blank=True, null=True)
    Slug = models.SlugField(unique=True,max_length=350, blank=True, null=True)  # Thêm slug
    Content = RichTextUploadingField(blank=True, null=True)
    Avatar = models.ImageField(upload_to='AVATAR_KQLS',null=True,blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

    def save(self, *args, **kwargs):
        if self.Slug:
            # Kiểm tra slug người dùng nhập đã chuẩn chưa
            normalized_slug = slugify(self.Slug)
            if self.Slug == normalized_slug:
                base_slug = self.Slug
            else:
                base_slug = normalized_slug
        else:
            # Không nhập slug → lấy theo Name
            base_slug = slugify(self.Title)

        slug = base_slug
        n = 1

        # Đảm bảo slug unique
        while (
            KqlsPost.objects.filter(Slug=slug).exclude(pk=self.pk).exists()
            or BlogPost.objects.filter(Slug=slug).exists()
            or Product.objects.filter(Slug=slug).exists()
        ):
            slug = f"{base_slug}-{n}"
            n += 1

        self.Slug = slug
        super().save(*args, **kwargs)

class Seo_Page(models.Model):
    Seo_Title = models.CharField(max_length=500, blank=True, null=True)
    Seo_Description = models.CharField(max_length=500, blank=True, null=True)
    Name_Page = models.CharField(max_length=50, blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)


    


