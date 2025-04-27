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
import uuid

    
def user_edit_admin(request,pk):
    if request.method == 'GET':
        if request.user.is_authenticated:
            context = {}
            context['domain'] = settings.DOMAIN
            try:
                context['obj_user'] = User.objects.get(pk=pk)
            except:
                context['obj_user'] = {}
            print('context:',context)
            if request.user.is_authenticated:
                return render(request, 'sleekweb/admin/user_edit_admin.html', context, status=200)
            else:
                return redirect('login_admin')
        return JsonResponse({'success': False, 'message': 'Log in to your account and make sure it has access'},json_dumps_params={'ensure_ascii': False})
    else:
        return redirect('user_edit_admin',pk=pk)
    

def user_change_password_admin(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            context = {}
            context['domain'] = settings.DOMAIN
            id = request.POST.get('id')
            new_password = request.POST.get('new_password')
            print('new_password:',new_password)
            try:
                if request.user.is_superuser:
                    obj = User.objects.get(pk=id)
                    obj.set_password(new_password)
                    obj.save()
                    update_session_auth_hash(request, obj)
                else:
                    obj = request.user
                    obj.set_password(new_password)
                return JsonResponse({'success': True,'message': f'Đổi mật khẩu thành công tài khoản {obj.username} !'},json_dumps_params={'ensure_ascii': False})
            except:
                obj = {}
                return JsonResponse({'success': True,'message': 'Tài khoản không tồn tại !'},json_dumps_params={'ensure_ascii': False})
        return JsonResponse({'success': False, 'message': 'Đăng nhập tài khoản và đảm bảo bạn có quyền truy cập'},json_dumps_params={'ensure_ascii': False})

