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


def change_dsdt_admin(request):
    if request.method == 'GET':
        context = {}
        context['domain'] = settings.DOMAIN
        context['list_Edit_dsdt_mb'] = Edit_dsdt.objects.filter(Category=0).order_by('Order')
        context['list_Edit_dsdt_mn'] = Edit_dsdt.objects.filter(Category=1).order_by('Order')
        context['Category'] = request.GET.get('Category')
        if not context['Category']:
            context['Category'] = '0'
        # print('context:',context)
        if request.user.is_authenticated and request.user.is_superuser:
            return render(request, 'sleekweb/admin/change_dsdt_admin.html', context, status=200)
        else:
            return JsonResponse({'success': False, 'message': 'Bạn chưa được cấp quyền do tài khoản chưa đăng nhập hoặc tài khoản không có quyền truy cập'})
    elif request.method == 'POST':
        if request.user.is_authenticated and request.user.is_superuser:
            fields = {}
            fields['Name'] = request.POST.get('Name')
            fields['Address'] = request.POST.get('Address')
            fields['Link'] = request.POST.get('Link')
            fields['Category'] = request.POST.get('Category')
            fields['Photo'] = request.FILES.get('Photo')
            fields['id'] = request.POST.get('id')
            try:
                obj = Edit_dsdt.objects.get(pk=fields['id'])
                for key, value in fields.items():
                    if value:
                        setattr(obj, key, value)
                obj.save()
            except:
                Edit_dsdt.objects.create(**fields)

            base_url = reverse('change_dsdt_admin')
            url = f"{base_url}?Category={fields['Category']}"
            return redirect(url)
        else:
            return JsonResponse({'success': False, 'message': 'Bạn chưa được cấp quyền do tài khoản chưa đăng nhập hoặc tài khoản không có quyền truy cập'})


def change_dsdt_order_admin(request):    
    if request.method == 'POST':
        context = {}
        id = request.POST.get('id')
        Order = request.POST.get('Order')
        try:
            obj = Edit_dsdt.objects.get(pk=id)
            obj.Order = Order
            obj.save()
        except:
            return redirect('change_dsdt_admin')
        return redirect('change_dsdt_admin')
    
def change_dsdt_remove_admin(request):    
    if request.method == 'POST':
        context = {}
        id = request.POST.get('id')
        Category = request.POST.get('Category')
        try:
            obj = Edit_dsdt.objects.get(pk=id)
            obj.delete()
        except:
            base_url = reverse('change_dsdt_admin')
            url = f"{base_url}?Category={Category}"
            return redirect(url)
        base_url = reverse('change_dsdt_admin')
        url = f"{base_url}?Category={Category}"
        return redirect(url)