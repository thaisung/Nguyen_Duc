from ...models import *

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_list_or_404, get_object_or_404
from django.core.paginator import Paginator


from django.http import HttpResponse
import requests
import time

from django.db import models
from django.utils import timezone

import os

from datetime import datetime

from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout

from django.contrib.postgres.search import TrigramSimilarity
from django.db.models import Q
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from datetime import datetime
from django.contrib import messages
import random
import string
from django.contrib.auth import update_session_auth_hash
from datetime import datetime, timedelta
from django.utils.timezone import make_aware

# from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

import random
import string

import base64

import time
from django.http import JsonResponse

import re
import json

from django.conf import settings
from django.db.models import Q

import datetime

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


import base64
from ...forms import *


    
def product_admin(request):
    if request.method == 'GET':
        context = {}
        context['domain'] = settings.DOMAIN
        context['list_Product'] = Product.objects.all()
        s = request.GET.get('s')
        if s:
            context['list_Product'] = context['list_Product'].filter(Q(Name__icontains=s)).order_by('-id')
            context['s'] = s
        
        context['obj_Seo_Page'] = Seo_Page.objects.filter(Name_Page='SP').first()

        # print('context:',context)
        if request.user.is_authenticated and request.user.is_superuser:
            return render(request, 'sleekweb/admin/product_admin.html', context, status=200)
        else:
            return redirect('login_admin')

def clean_describe(describe):
    # Bước 1: Tạm thời thay thế các &nbsp; mà đứng một mình trong thẻ thành placeholder để giữ lại
    describe = re.sub(r'>(\s*&nbsp;\s*)<', r'>__NBSP_PLACEHOLDER__<', describe)

    # Bước 2: Thay tất cả các &nbsp; còn lại thành dấu cách
    describe = describe.replace('&nbsp;', ' ')

    # Bước 3: Khôi phục lại các placeholder thành &nbsp;
    describe = describe.replace('__NBSP_PLACEHOLDER__', '&nbsp;')

    return describe

def product_add_admin(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    if request.method == 'GET':
        form = ProductForm()
        context = {
        'form': form,
        # 'list_Product': Product.objects.all()
        }
        return render(request, 'sleekweb/admin/product_add_admin.html',context, status=200)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():   # BẮT BUỘC PHẢI CÓ

            # Lấy describe
            describe = form.cleaned_data.get('Describe')

            # Làm sạch
            cleaned_describe = clean_describe(describe)

            # CHƯA save ngay
            product = form.save(commit=False)

            product.Describe = cleaned_describe
            product.save()

            # LẤY DANH SÁCH ẢNH
            List_Photo = request.FILES.getlist('List_Photo')
            List_Photo_NCLS = request.FILES.getlist('List_Photo_NCLS')

            for img in List_Photo:
                Photo.objects.create(
                    Avatar=img,
                    Belong_Product=product
                )

            for img in List_Photo_NCLS:
                Photo_ncls.objects.create(
                    Avatar=img,
                    Belong_Product=product
                )

            return redirect('product_admin')

        else:
            print(form.errors)  # debug nếu cần

def product_edit_admin(request, pk):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    obj_Product = Product.objects.get(pk=pk)  # Lấy bài viết theo pk

    if request.method == 'GET':
        form = ProductForm(instance=obj_Product)  # Gán instance
        context = {
            'form': form,
            'obj_Product': obj_Product,
            # 'list_Product': Product.objects.all()
        }
        return render(request, 'sleekweb/admin/product_edit_admin.html', context, status=200)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=obj_Product)  # Cập nhật đúng bài viết
        if form.is_valid():
            # Lấy describe
            describe = form.cleaned_data.get('Describe')

            # Làm sạch
            cleaned_describe = clean_describe(describe)

            # CHƯA save ngay
            product = form.save(commit=False)

            product.Describe = cleaned_describe
            product.save()

            # LẤY DANH SÁCH ẢNH
            List_Photo = request.FILES.getlist('List_Photo')
            List_Photo_NCLS = request.FILES.getlist('List_Photo_NCLS')
            if List_Photo:
                product.list_photo.all().delete()
                for img in List_Photo:
                    Photo.objects.create(
                        Avatar=img,
                        Belong_Product=product
                    )
            if List_Photo_NCLS:
                product.list_photo_ncls.all().delete()
                for img in List_Photo_NCLS:
                    Photo_ncls.objects.create(
                        Avatar=img,
                        Belong_Product=product
                    )

            return redirect('product_edit_admin',pk=pk)  # hoặc chuyển đến nơi khác

# def product_add_admin(request):
#     if request.method == 'GET':
#         context = {}
#         context['domain'] = settings.DOMAIN
#         # print('context:',context)
#         if request.user.is_authenticated and request.user.is_superuser:
#             return render(request, 'sleekweb/admin/product_add_admin.html', context, status=200)
#         else:
#             return redirect('login_admin')
        
#     elif request.method == 'POST':
#         fields = {}
#         fields['Slug']= request.POST.get('Slug')
#         fields['Seo_Title']= request.POST.get('Seo_Title')
#         fields['Seo_Description']= request.POST.get('Seo_Description')
#         fields['Avatar']= request.FILES.get('Avatar')
#         fields['Name'] = request.POST.get('Name')
#         fields['Title'] = request.POST.get('Title')
#         fields['Category'] = request.POST.get('Category')
#         # fields['Price'] = request.POST.get('Price')
#         fields['Introduce'] = request.POST.get('Introduce')
#         fields['Describe'] = request.POST.get('Describe')
#         fields['Main_ingredients'] = request.POST.get('Main_ingredients')
#         fields['How_use'] = request.POST.get('How_use')
#         # fields['Ingredients_table'] = request.POST.get('Ingredients_table')
#         List_Photo= request.FILES.getlist('List_Photo')
#         List_Photo_NCLS= request.FILES.getlist('List_Photo_NCLS')
#         obj = Product.objects.create(**fields)
#         if obj and List_Photo:
#             for i in List_Photo:
#                 Photo.objects.create(Avatar=i,Belong_Product=obj)
#         if obj and List_Photo_NCLS:
#             for j in List_Photo_NCLS:
#                 Photo_ncls.objects.create(Avatar=j,Belong_Product=obj)
#         return redirect('product_admin')
    
# def product_edit_admin(request,pk):
#     if request.method == 'GET':
#         context = {}
#         context['domain'] = settings.DOMAIN
#         context['obj_Product'] = Product.objects.get(pk=pk)
#         # print('context:',context)
#         if request.user.is_authenticated and request.user.is_superuser:
#             return render(request, 'sleekweb/admin/product_edit_admin.html', context, status=200)
#         else:
#             return redirect('login_admin')
#     elif request.method == 'POST':
#         fields = {}
#         # fields['id']= request.FILES.get('id')
#         fields['Slug']= request.POST.get('Slug')
#         fields['Seo_Title']= request.POST.get('Seo_Title')
#         fields['Seo_Description']= request.POST.get('Seo_Description')
#         fields['Avatar']= request.FILES.get('Avatar')
#         fields['Name'] = request.POST.get('Name')
#         fields['Title'] = request.POST.get('Title')
#         fields['Category'] = request.POST.get('Category')
#         # fields['Price'] = request.POST.get('Price')
#         fields['Introduce'] = request.POST.get('Introduce')
#         fields['Describe'] = request.POST.get('Describe')
#         fields['Main_ingredients'] = request.POST.get('Main_ingredients')
#         fields['How_use'] = request.POST.get('How_use')
#         # fields['Ingredients_table'] = request.POST.get('Ingredients_table')
#         List_Photo= request.FILES.getlist('List_Photo')
#         List_Photo_NCLS= request.FILES.getlist('List_Photo_NCLS')
#         # if fields['id']:
#         obj = Product.objects.get(pk=pk)
#         obj.Name = fields['Name']
#         obj.Title = fields['Title']
#         obj.Slug = fields['Slug']
#         obj.Seo_Title = fields['Seo_Title']
#         obj.Seo_Description = fields['Seo_Description']
#         obj.Category = fields['Category']
#         # obj.Price = fields['Price']
#         obj.Introduce = fields['Introduce'] 
#         obj.Describe = fields['Describe']
#         obj.Main_ingredients = fields['Main_ingredients'] 
#         obj.How_use = fields['How_use'] 
#         # obj.Ingredients_table = fields['Ingredients_table']
#         if fields['Avatar']:
#             obj.Avatar = fields['Avatar']
#         obj.save()
#         if List_Photo:
#             obj.list_photo.all().delete()
#             for i in List_Photo:
#                 Photo.objects.create(Avatar=i,Belong_Product=obj)
#         if List_Photo_NCLS:
#             obj.list_photo_ncls.all().delete()
#             for j in List_Photo_NCLS:
#                 Photo_ncls.objects.create(Avatar=j,Belong_Product=obj)
#         return redirect('product_edit_admin',pk=pk)
    
def product_remove_admin(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        try:
            obj = Product.objects.get(pk=id)
            obj.delete()
        except:
            print('not')
        return redirect('product_admin')
    

def size_product_add_admin(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        Name = request.POST.get('Name')
        Price = request.POST.get('Price')
        try:
            obj = Product.objects.get(pk=id)
            Size.objects.create(Name=Name,Price=Price,Belong_Product=obj)
        except:
            print('not')
        return redirect('product_admin')
    
def size_product_remove_admin(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        try:
            obj = Size.objects.get(pk=id)
            obj.delete()
        except:
            print('not')
        return redirect('product_admin')