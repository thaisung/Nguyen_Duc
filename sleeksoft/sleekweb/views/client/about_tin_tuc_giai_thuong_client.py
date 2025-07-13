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


def about_tin_tuc_giai_thuong_client(request):
    if request.method == 'GET':
        context = {}
        context['domain'] = settings.DOMAIN
        try:
            context['obj'] = Website.objects.get(Count=1)
        except:
            context['obj'] = {}
        try:
            context['obj1'] = Edit_ttgt.objects.get(Count=1)
        except:
            context['obj1'] = {}
        context['list_Edit_ttgt1'] = Edit_ttgt1.objects.all().order_by('Order')
        context['list_Product'] = Product.objects.all()
        context['list_image_slider_3'] = Photo_Slider.objects.filter(Count=3)
        # print('context:',context)
        return render(request, 'sleekweb/client/about_tin_tuc_giai_thuong_client.html', context, status=200)
    
def about_tin_tuc_giai_thuong_detail_client(request,slug):
    if request.method == 'GET':
        context = {}
        context['domain'] = settings.DOMAIN
        try:
            context['obj'] = Website.objects.get(Count=1)
        except:
            context['obj'] = {}
        try:
            context['obj1'] = Edit_ttgt1.objects.get(Slug=slug)
        except:
            context['obj1'] = {}
        context['list_ttgt1'] = Edit_ttgt1.objects.all().order_by('-id')
        context['list_Product'] = Product.objects.all()
        context['list_image_slider_3'] = Photo_Slider.objects.filter(Count=3)
        # print('context:',context)
        return render(request, 'sleekweb/client/link_tt_gt_1_client.html', context, status=200)

def link_tt_gt_1_client(request):
    if request.method == 'GET':
        context = {}
        context['domain'] = settings.DOMAIN
        context['list_Product'] = Product.objects.all()
        context['list_image_slider_3'] = Photo_Slider.objects.filter(Count=3)
        # print('context:',context)
        return render(request, 'sleekweb/client/link_tt_gt_1_client.html', context, status=200)
    
def link_tt_gt_2_client(request):
    if request.method == 'GET':
        context = {}
        context['domain'] = settings.DOMAIN
        context['list_Product'] = Product.objects.all()
        context['list_image_slider_3'] = Photo_Slider.objects.filter(Count=3)
        # print('context:',context)
        return render(request, 'sleekweb/client/link_tt_gt_2_client.html', context, status=200)