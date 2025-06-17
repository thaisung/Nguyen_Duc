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

def change_kqls_post_admin(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    if request.method == 'GET':
        form = KqlsPostForm()
        context = {
        'form': form,
        }
        list_KqlsPost =KqlsPost.objects.all().order_by('-id')
        s = request.GET.get('s')
        if s:
            list_KqlsPost = list_KqlsPost.filter(Q(Title__icontains=s)).order_by('-id')
            context['s'] = s
        p = request.GET.get('p','1')
        context['p'] = p
        # Sử dụng Paginator để chia nhỏ danh sách (10 là số lượng mục trên mỗi trang)
        paginator = Paginator(list_KqlsPost, settings.PAGE)
        # Lấy số trang hiện tại từ URL, nếu không mặc định là trang 1
        context['list_KqlsPost'] = paginator.get_page(p)
        return render(request, 'sleekweb/admin/change_kqls_post_admin.html',context, status=200)

def clean_content(content):
    # Bước 1: Tạm thời thay thế các &nbsp; mà đứng một mình trong thẻ thành placeholder để giữ lại
    content = re.sub(r'>(\s*&nbsp;\s*)<', r'>__NBSP_PLACEHOLDER__<', content)

    # Bước 2: Thay tất cả các &nbsp; còn lại thành dấu cách
    content = content.replace('&nbsp;', ' ')

    # Bước 3: Khôi phục lại các placeholder thành &nbsp;
    content = content.replace('__NBSP_PLACEHOLDER__', '&nbsp;')

    return content

def change_kqls_post_add_admin(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    if request.method == 'GET':
        form = KqlsPostForm()
        context = {
        'form': form,
        # 'list_KqlsPost': KqlsPost.objects.all()
        }
        return render(request, 'sleekweb/admin/change_kqls_post_add_admin.html',context, status=200)
    if request.method == 'POST':
        form = KqlsPostForm(request.POST, request.FILES)  # BẮT BUỘC phải có request.FILES
        if form.is_valid():
            # Lấy nội dung từ form
            content = form.cleaned_data['Content']
            
            # Làm sạch nội dung trước khi lưu
            cleaned_content = clean_content(content)
            # cleaned_content = content
            
            # Lưu vào model (hoặc xử lý thêm nếu cần)
            form.instance.Content = cleaned_content
            form.save()
            return redirect('change_kqls_post_admin')  # hoặc chuyển đến trang khác


def change_kqls_post_edit_admin(request, pk):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    obj_Blog = KqlsPost.objects.get(pk=pk)  # Lấy bài viết theo pk

    if request.method == 'GET':
        form = KqlsPostForm(instance=obj_Blog)  # Gán instance
        context = {
            'form': form,
            'obj_Blog': obj_Blog,
            # 'list_KqlsPost': KqlsPost.objects.all()
        }
        return render(request, 'sleekweb/admin/change_kqls_post_edit_admin.html', context, status=200)

    if request.method == 'POST':
        form = KqlsPostForm(request.POST, request.FILES, instance=obj_Blog)  # Cập nhật đúng bài viết
        if form.is_valid():
            # Lấy nội dung từ form
            content = form.cleaned_data['Content']
            
            # Làm sạch nội dung trước khi lưu
            cleaned_content = clean_content(content)
            # cleaned_content = content
            
            # Lưu vào model (hoặc xử lý thêm nếu cần)
            form.instance.Content = cleaned_content

            form.save()
            return redirect('change_kqls_post_admin')  # hoặc chuyển đến nơi khác
        
def change_kqls_post_remove_admin(request, pk):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    obj_Blog = KqlsPost.objects.get(pk=pk)  # Lấy bài viết theo pk

    if request.method == 'GET':
        form = KqlsPostForm(instance=obj_Blog)  # Gán instance
        obj_Blog.delete()
        return redirect('change_kqls_post_admin')



# def change_detail_blog(request,pk):
#     context = {
#     'obj_Blog': KqlsPost.objects.get(pk=pk)
#     }
#     return render(request, 'sleekweb/admin/change_kqls_post_admin.html',context, status=200)
