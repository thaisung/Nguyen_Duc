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


def change_ttgt_admin(request):
    if request.method == 'GET':
        context = {}
        context['domain'] = settings.DOMAIN

        form = ttgt1Form()
        context = {
        'form': form,
        }
        list_Edit_ttgt1 =Edit_ttgt1.objects.all().order_by('Order')
        s = request.GET.get('s')
        if s:
            list_Edit_ttgt1 = list_Edit_ttgt1.filter(Q(Title__icontains=s)).order_by('Order')
            context['s'] = s
        p = request.GET.get('p','1')
        context['p'] = p
        # Sử dụng Paginator để chia nhỏ danh sách (10 là số lượng mục trên mỗi trang)
        paginator = Paginator(list_Edit_ttgt1, settings.PAGE)
        # Lấy số trang hiện tại từ URL, nếu không mặc định là trang 1
        context['list_Edit_ttgt1'] = paginator.get_page(p)
        context['list_Edit_ttgt1'] = list_Edit_ttgt1

        try:
            context['obj'] = Edit_ttgt.objects.get(Count=1)
        except:
            context['obj'] = {}

        # print('context:',context)
        if request.user.is_authenticated and request.user.is_superuser:
            return render(request, 'sleekweb/admin/change_ttgt_admin.html', context, status=200)
        else:
            return JsonResponse({'success': False, 'message': 'Bạn chưa được cấp quyền do tài khoản chưa đăng nhập hoặc tài khoản không có quyền truy cập'})
    elif request.method == 'POST':
        if request.user.is_authenticated and request.user.is_superuser:
            fields = {}
            fields['Title1'] = request.POST.get('Title1')
            fields['Photo1'] = request.FILES.get('Photo1')
            try:
                obj = Edit_ttgt.objects.get(Count=1)
                for key, value in fields.items():
                    if value:
                        setattr(obj, key, value)
                obj.save()
            except:
                fields['Count'] = 1
                Edit_ttgt.objects.create(**fields)
            return redirect('change_ttgt_admin')
        else:
            return JsonResponse({'success': False, 'message': 'Bạn chưa được cấp quyền do tài khoản chưa đăng nhập hoặc tài khoản không có quyền truy cập'})

def change_ttgt1_admin(request):
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.is_superuser:
            fields = {}
            fields['id'] = request.GET.get('id')
            try:
                if fields['id']:
                    obj = Edit_ttgt1.objects.get(id=fields['id'])
                    obj.delete()
            except:
                print('Not obj')
            return redirect('change_ttgt_admin')
def clean_content(content):
    # Loại bỏ các ký tự &nbsp; và thay thế bằng khoảng trắng thông thường
    content = content.replace('&nbsp;', ' ')
    
    # # Loại bỏ các thẻ HTML không mong muốn (có thể thêm hoặc chỉnh sửa tùy ý)
    # content = re.sub(r'<script.*?>.*?</script>', '', content, flags=re.DOTALL)  # Loại bỏ thẻ script
    # content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)  # Loại bỏ bình luận HTML

    # # Thêm bất kỳ xử lý làm sạch nào khác nếu cần
    
    return content


def change_ttgt1_add_admin(request):
    if request.method == 'GET':
        form = ttgt1Form()
        context = {
        'form': form,
        }
        return render(request, 'sleekweb/admin/change_ttgt1_add_admin.html',context, status=200)
    if request.method == 'POST':
        form = ttgt1Form(request.POST, request.FILES)  # BẮT BUỘC phải có request.FILES
        if form.is_valid():
            # Lấy nội dung từ form
            content = form.cleaned_data['Content']
            
            # Làm sạch nội dung trước khi lưu
            cleaned_content = clean_content(content)
            
            # Lưu vào model (hoặc xử lý thêm nếu cần)
            form.instance.Content = cleaned_content
            form.save()
            return redirect('change_ttgt_admin')  # hoặc chuyển đến trang khác

def change_ttgt1_edit_admin(request, pk):
    obj_ttgt1 = Edit_ttgt1.objects.get(pk=pk)  # Lấy bài viết theo pk

    if request.method == 'GET':
        form = ttgt1Form(instance=obj_ttgt1)  # Gán instance
        context = {
            'form': form,
            'obj_ttgt1': obj_ttgt1,
        }
        return render(request, 'sleekweb/admin/change_ttgt1_edit_admin.html', context, status=200)

    if request.method == 'POST':
        form = ttgt1Form(request.POST, request.FILES, instance=obj_ttgt1)  # Cập nhật đúng bài viết
        if form.is_valid():
            # Lấy nội dung từ form
            content = form.cleaned_data['Content']
            
            # Làm sạch nội dung trước khi lưu
            cleaned_content = clean_content(content)
            
            # Lưu vào model (hoặc xử lý thêm nếu cần)
            form.instance.Content = cleaned_content
            form.save()
            return redirect('change_ttgt_admin')  # hoặc chuyển đến nơi khác
        
def change_ttgt1_remove_admin(request, pk):
    obj_ttgt1 = Edit_ttgt1.objects.get(pk=pk)  # Lấy bài viết theo pk

    if request.method == 'GET':
        obj_ttgt1.delete()
        return redirect('change_ttgt_admin')

def change_ttgt1_order_admin(request):    
    if request.method == 'POST':
        context = {}
        id = request.POST.get('id')
        Order = request.POST.get('Order')
        try:
            obj = Edit_ttgt1.objects.get(pk=id)
            obj.Order = Order
            obj.save()
        except:
            return redirect('change_ttgt_admin')
        return redirect('change_ttgt_admin')