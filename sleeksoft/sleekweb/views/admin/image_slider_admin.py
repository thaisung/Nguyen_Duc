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



    
def image_slider_admin(request):
    if request.method == 'GET':
        context = {}
        context['domain'] = settings.DOMAIN
        context['list_image_slider_1'] = Photo_Slider.objects.filter(Count=1)
        context['list_image_slider_2'] = Photo_Slider.objects.filter(Count=2)
        context['list_image_slider_3'] = Photo_Slider.objects.filter(Count=3)
        return render(request, 'sleekweb/admin/image_slider_admin.html', context, status=200)
    if request.method == 'POST':
        context = {}
        Count = request.POST.get('Count')
        list_image_slider_1 = request.FILES.getlist('list_image_slider_1')
        list_image_slider_2 = request.FILES.getlist('list_image_slider_2')
        list_image_slider_3 = request.FILES.getlist('list_image_slider_3')
        if int(Count) == 1 and list_image_slider_1:
            for i in list_image_slider_1:
                Photo_Slider.objects.create(Photo=i,Count=1)
        if int(Count) == 2 and list_image_slider_2:
            for i in list_image_slider_2:
                Photo_Slider.objects.create(Photo=i,Count=2)
        if int(Count) == 3 and list_image_slider_3:
            for i in list_image_slider_3:
                Photo_Slider.objects.create(Photo=i,Count=3)
        return redirect('image_slider_admin')
        


# def product_add_admin(request):
#     if request.method == 'GET':
#         context = {}
#         context['domain'] = settings.DOMAIN
#         print('context:',context)
#         return render(request, 'sleekweb/admin/product_add_admin.html', context, status=200)
#     elif request.method == 'POST':
#         fields = {}
#         fields['Avatar']= request.FILES.get('Avatar')
#         fields['Name'] = request.POST.get('Name')
#         fields['Category'] = request.POST.get('Category')
#         fields['Price'] = request.POST.get('Price')
#         fields['Introduce'] = request.POST.get('Introduce')
#         fields['Describe'] = request.POST.get('Describe')
#         fields['Main_ingredients'] = request.POST.get('Main_ingredients')
#         fields['How_use'] = request.POST.get('How_use')
#         fields['Ingredients_table'] = request.POST.get('Ingredients_table')
#         List_Photo= request.FILES.getlist('List_Photo')
#         List_Photo_NCLS= request.FILES.getlist('List_Photo_NCLS')
#         obj = Product.objects.create(**fields)
#         if obj and List_Photo:
#             for i in List_Photo:
#                 Photo.objects.create(Avatar=i,Belong_Product=obj)
#         if obj and List_Photo_NCLS:
#             for j in List_Photo_NCLS:
#                 Photo_ncls.objects.create(Avatar=j,Belong_Product=obj)
#         return redirect('product_admin')
    
# def product_edit_admin(request,pk):
#     if request.method == 'GET':
#         context = {}
#         context['domain'] = settings.DOMAIN
#         context['obj_Product'] = Product.objects.get(pk=pk)
#         print('context:',context)
#         return render(request, 'sleekweb/admin/product_edit_admin.html', context, status=200)
#     elif request.method == 'POST':
#         fields = {}
#         # fields['id']= request.FILES.get('id')
#         fields['Avatar']= request.FILES.get('Avatar')
#         fields['Name'] = request.POST.get('Name')
#         fields['Category'] = request.POST.get('Category')
#         fields['Price'] = request.POST.get('Price')
#         fields['Introduce'] = request.POST.get('Introduce')
#         fields['Describe'] = request.POST.get('Describe')
#         fields['Main_ingredients'] = request.POST.get('Main_ingredients')
#         fields['How_use'] = request.POST.get('How_use')
#         fields['Ingredients_table'] = request.POST.get('Ingredients_table')
#         List_Photo= request.FILES.getlist('List_Photo')
#         List_Photo_NCLS= request.FILES.getlist('List_Photo_NCLS')
#         # if fields['id']:
#         obj = Product.objects.get(pk=pk)
#         obj.Name = fields['Name']
#         obj.Category = fields['Category']
#         obj.Price = fields['Price']
#         obj.Introduce = fields['Introduce'] 
#         obj.Describe = fields['Describe']
#         obj.Main_ingredients = fields['Main_ingredients'] 
#         obj.How_use = fields['How_use'] 
#         obj.Ingredients_table = fields['Ingredients_table']
#         if fields['Avatar']:
#             obj.Avatar = fields['Avatar']
#         obj.save()
#         if List_Photo:
#             obj.list_photo.all().delete()
#             for i in List_Photo:
#                 Photo.objects.create(Avatar=i,Belong_Product=obj)
#         if List_Photo_NCLS:
#             obj.list_photo_ncls.all().delete()
#             for j in List_Photo_NCLS:
#                 Photo_ncls.objects.create(Avatar=j,Belong_Product=obj)
#         return redirect('product_edit_admin',pk=pk)
    
# def product_remove_admin(request):
#     if request.method == 'POST':
#         id = request.POST.get('id')
#         try:
#             obj = Product.objects.get(pk=id)
#             obj.delete()
#         except:
#             print('not')
#         return redirect('product_admin')
    

# def size_product_add_admin(request):
#     if request.method == 'POST':
#         id = request.POST.get('id')
#         Name = request.POST.get('Name')
#         try:
#             obj = Product.objects.get(pk=id)
#             Size.objects.create(Name=Name,Belong_Product=obj)
#         except:
#             print('not')
#         return redirect('product_admin')
    
# def size_product_remove_admin(request):
#     if request.method == 'POST':
#         id = request.POST.get('id')
#         try:
#             obj = Size.objects.get(pk=id)
#             obj.delete()
#         except:
#             print('not')
#         return redirect('product_admin')