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


def clean_content(content):
    # Bước 1: Tạm thời thay thế các &nbsp; mà đứng một mình trong thẻ thành placeholder để giữ lại
    content = re.sub(r'>(\s*&nbsp;\s*)<', r'>__NBSP_PLACEHOLDER__<', content)

    # Bước 2: Thay tất cả các &nbsp; còn lại thành dấu cách
    content = content.replace('&nbsp;', ' ')

    # Bước 3: Khôi phục lại các placeholder thành &nbsp;
    content = content.replace('__NBSP_PLACEHOLDER__', '&nbsp;')

    return content

def change_kqls1_admin(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    if request.method == 'GET':
        try:
            obj = Edit_kqls1.objects.get(Order=1)
        except:
            obj = Edit_kqls1.objects.create(Content='',Order=1)
        form = Edit_kqls1_Form(instance=obj)  # Gán instance
        context = {
            'form': form,
            'obj': obj,
        }
        return render(request, 'sleekweb/admin/change_kqls1_admin.html', context, status=200)
    if request.method == 'POST':
        obj = Edit_kqls1.objects.get(Order=1)
        form = Edit_kqls1_Form(request.POST, request.FILES, instance=obj)  # Cập nhật đúng bài viết
        if form.is_valid():
            # Lấy nội dung từ form
            content = form.cleaned_data['Content']
            
            # Làm sạch nội dung trước khi lưu
            cleaned_content = clean_content(content)
            # cleaned_content = content
            
            # Lưu vào model (hoặc xử lý thêm nếu cần)
            form.instance.Content = cleaned_content

            form.save()
            return redirect('change_kqls1_admin')  # hoặc chuyển đến nơi khác