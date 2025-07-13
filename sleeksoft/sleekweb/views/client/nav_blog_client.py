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

from django.core.mail import send_mail
from django.forms.models import model_to_dict
from django.core.mail import send_mail,EmailMessage



    
def nav_blog_client(request):
    if request.method == 'GET':
        context = {}
        context['domain'] = settings.DOMAIN
        try:
            context['obj'] = Website.objects.get(Count=1)
        except:
            context['obj'] = {}

        context['list_BlogPost'] =  BlogPost.objects.all().order_by('-id')
        s = request.GET.get('s')
        if s:
            context['list_BlogPost'] = context['list_BlogPost'].filter(Q(Title__icontains=s)).order_by('-id')
            context['s'] = s
        p = request.GET.get('p','1')
        context['p'] = p
        # Sử dụng Paginator để chia nhỏ danh sách (10 là số lượng mục trên mỗi trang)
        paginator = Paginator(context['list_BlogPost'], settings.PAGE)
        # Lấy số trang hiện tại từ URL, nếu không mặc định là trang 1
        context['list_BlogPost'] = paginator.get_page(p)

        context['list_image_slider_3'] = Photo_Slider.objects.filter(Count=3)
        # try:
        #     context['obj_Count_2'] = Photo_Content.objects.get(Count=2)
        # except:
        #     context['obj_Count_2'] = {}
        try:
            context['obj_Count_3'] = Photo_Content.objects.get(Count=3)
        except:
            context['obj_Count_3'] = {}
        try:
            context['obj_Count_4'] = Photo_Content.objects.get(Count=4)
        except:
            context['obj_Count_4'] = {}
        try:
            context['obj_Count_5'] = Photo_Content.objects.get(Count=5)
        except:
            context['obj_Count_5'] = {}
        context['list_Product'] = Product.objects.all().order_by('-id')
        # print('context:',context)
        return render(request, 'sleekweb/client/nav_blog_client.html', context, status=200)
    
def nav_blog_detail_client(request,slug):
    if request.method == 'GET':
        context = {}
        
        try:
            context['obj'] = Website.objects.get(Count=1)
        except:
            context['obj'] = {}

        context['list_BlogPost'] =  BlogPost.objects.all().order_by('-id')

        try:
            context['obj_Blog'] = BlogPost.objects.get(Slug=slug)
        except BlogPost.DoesNotExist:
            # Trả về redirect về trang chủ hoặc trang 404 tùy ý
            return redirect('/')

        context['list_Product'] = Product.objects.all().order_by('-id')
        return render(request, 'sleekweb/client/nav_blog_detail_client.html', context, status=200)