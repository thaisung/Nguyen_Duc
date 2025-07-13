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


def change_vct_admin(request):
    if request.method == 'GET':
        context = {}
        context['domain'] = settings.DOMAIN
        try:
            context['obj'] = Edit_vct.objects.get(Count=1)
        except:
            context['obj'] = {}
        context['list_Edit_vct1'] = Edit_vct1.objects.all().order_by('Order')
        # print('context:',context)
        if request.user.is_authenticated and request.user.is_superuser:
            return render(request, 'sleekweb/admin/change_vct_admin.html', context, status=200)
        else:
            return JsonResponse({'success': False, 'message': 'Bạn chưa được cấp quyền do tài khoản chưa đăng nhập hoặc tài khoản không có quyền truy cập'})
    elif request.method == 'POST':
        if request.user.is_authenticated and request.user.is_superuser:
            fields = {}
            fields['Title1'] = request.POST.get('Title1')
            fields['Content1'] = request.POST.get('Content1')
            fields['Content2'] = request.POST.get('Content2')
            fields['Title2'] = request.POST.get('Title2')
            fields['Content3'] = request.POST.get('Content3')
            fields['Photo1'] = request.FILES.get('Photo1')
            fields['Photo2'] = request.FILES.get('Photo2')
            fields['Photo3'] = request.FILES.get('Photo3')
            try:
                obj = Edit_vct.objects.get(Count=1)
                for key, value in fields.items():
                    if value:
                        setattr(obj, key, value)
                obj.save()
            except:
                fields['Count'] = 1
                Edit_vct.objects.create(**fields)
            return redirect('change_vct_admin')
        else:
            return JsonResponse({'success': False, 'message': 'Bạn chưa được cấp quyền do tài khoản chưa đăng nhập hoặc tài khoản không có quyền truy cập'})

def change_vct1_admin(request):
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.is_superuser:
            fields = {}
            fields['id'] = request.GET.get('id')
            try:
                if fields['id']:
                    obj = Edit_vct1.objects.get(id=fields['id'])
                    obj.delete()
            except:
                print('Not obj')
            return redirect('change_vct_admin')
    if request.method == 'POST':
        if request.user.is_authenticated and request.user.is_superuser:
            fields = {}
            fields['Title'] = request.POST.get('Title')
            fields['Content'] = request.POST.get('Content')
            fields['Photo'] = request.FILES.get('Photo')
            fields['id'] = request.POST.get('id')
            if fields['id']:
                try:
                    obj = Edit_vct1.objects.get(id=fields['id'])
                    for key, value in fields.items():
                        if value:
                            setattr(obj, key, value)
                    obj.save()
                except:
                    print('Not obj')
            else:
                Edit_vct1.objects.create(**fields)
            return redirect('change_vct_admin')
        else:
            return JsonResponse({'success': False, 'message': 'Bạn chưa được cấp quyền do tài khoản chưa đăng nhập hoặc tài khoản không có quyền truy cập'})

def change_vct1_order_admin(request):    
    if request.method == 'POST':
        context = {}
        id = request.POST.get('id')
        Order = request.POST.get('Order')
        try:
            obj = Edit_vct1.objects.get(pk=id)
            obj.Order = Order
            obj.save()
        except:
            return redirect('change_vct_admin')
        return redirect('change_vct_admin')