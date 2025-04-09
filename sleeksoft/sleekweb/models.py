from django.db import models

# Create your models here.
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin

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
    
    Avatar = models.ImageField(upload_to='PRODUCT_AVATAR',null=True,blank=True)
    Name = models.CharField('Tên SP', max_length=500,blank=True, null=True)
    Category = models.CharField('Danh mục', max_length=250,blank=True, null=True)
    Price = models.CharField('Giá', max_length=255,blank=True, null=True)
    Introduce = models.TextField('Giới thiệu',blank=True, null=True)
    Describe = models.TextField('Mô tả',blank=True, null=True)
    Main_ingredients = models.TextField('Thành phần chính',blank=True, null=True)
    How_use = models.TextField('Cách sử dụng',blank=True, null=True)
    Ingredients_table = models.TextField('Bảng thành phần',blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

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
    Photo3 = models.ImageField(upload_to='PHOTO_CONTENT',null=True,blank=True)
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
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)


# class Banner(models.Model):
#     class Meta:
#         ordering = ["id"]
#         verbose_name_plural = "Ảnh Banner"
    
#     Photo = models.ImageField(upload_to='website/banner',null=True,blank=True)
#     Belong_Website = models.ForeignKey(Website, on_delete=models.CASCADE, related_name='list_photo_banner',blank=True, null=True)
#     Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
#     Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    


