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



import os
import json
from django.http import JsonResponse

import os
import json
from django.http import JsonResponse

def add_dsdt_mb(request):
    Edit_dsdt.objects.filter(Category='0').delete()
    # Lấy đường dẫn tuyệt đối đến thư mục chứa script api.py
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Tạo đường dẫn đầy đủ đến file mb.json
    file_path = os.path.join(current_directory, 'mb.json')

    # Kiểm tra sự tồn tại của file
    if not os.path.exists(file_path):
        return JsonResponse({'success': False, 'message': f"File {file_path} không tồn tại!"})

    if request.method == 'GET':
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for i in data:
            i['Category'] = '0'
            Edit_dsdt.objects.create(**i)

        return JsonResponse({'success': True, 'message': 'Add data miền bắc thành công'})

    return JsonResponse({'success': False, 'message': 'Phương thức không được hỗ trợ'})

def add_dsdt_mn(request):
    Edit_dsdt.objects.filter(Category='1').delete()
    # Lấy đường dẫn tuyệt đối đến thư mục chứa script api.py
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Tạo đường dẫn đầy đủ đến file mb.json
    file_path = os.path.join(current_directory, 'mn.json')

    # Kiểm tra sự tồn tại của file
    if not os.path.exists(file_path):
        return JsonResponse({'success': False, 'message': f"File {file_path} không tồn tại!"})

    if request.method == 'GET':
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for i in data:
            i['Category'] = '1'
            Edit_dsdt.objects.create(**i)

        return JsonResponse({'success': True, 'message': 'Add data miền nam thành công'})

    return JsonResponse({'success': False, 'message': 'Phương thức không được hỗ trợ'})
    


    
