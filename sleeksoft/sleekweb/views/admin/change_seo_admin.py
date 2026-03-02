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

from django.shortcuts import redirect

        
def change_seo_page_admin(request):
    if request.method == 'POST':
        if request.user.is_authenticated and request.user.is_superuser:
            fields = {
                'Seo_Title': request.POST.get('Seo_Title'),
                'Seo_Description': request.POST.get('Seo_Description'),
                'Name_Page': request.POST.get('Name_Page'),
            }

            try:
                obj = Seo_Page.objects.get(Name_Page=fields['Name_Page'])
                for key, value in fields.items():
                    if value:
                        setattr(obj, key, value)
                obj.save()
            except Seo_Page.DoesNotExist:
                fields['Name_Page'] = fields.get('Name_Page')
                Seo_Page.objects.create(**fields)

            # ✅ QUAY LẠI TRANG VỪA POST
            return redirect(request.META.get('HTTP_REFERER', '/'))

        return JsonResponse({
            'success': False,
            'message': 'Bạn chưa được cấp quyền do tài khoản chưa đăng nhập hoặc tài khoản không có quyền truy cập'
        })