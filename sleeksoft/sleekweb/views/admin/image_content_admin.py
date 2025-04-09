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



    
def image_content_admin(request):
    if request.method == 'GET':
        context = {}
        context['domain'] = settings.DOMAIN

        try:
            context['obj_Count_1'] = Photo_Content.objects.get(Count=1)
        except:
            context['obj_Count_1'] = {}

        try:
            context['obj_Count_2'] = Photo_Content.objects.get(Count=2)
        except:
            context['obj_Count_2'] = {}

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

        try:
            context['obj_Count_6'] = Photo_Content.objects.get(Count=6)
        except:
            context['obj_Count_6'] = {}
        
        return render(request, 'sleekweb/admin/image_content_admin.html', context, status=200)
    if request.method == 'POST':
        context = {}
        fields = {}
        Count = request.POST.get('Count')

        # 1.Trang chủ
        fields['Photo1'] = request.FILES.get('Photo1')
        fields['Content1'] = request.POST.get('Content1')
        fields['Photo2'] = request.FILES.get('Photo2')
        fields['Content2'] = request.POST.get('Content2')
        fields['Photo3'] = request.FILES.get('Photo3')
        fields['Content3'] = request.POST.get('Content3')
        if int(Count) == 1:
            try:
                context['obj_Count_1'] = Photo_Content.objects.get(Count=1)
            except:
                context['obj_Count_1'] = {}
            if context['obj_Count_1']:
                context['obj_Count_1'].Content1 = fields['Content1']
                if fields['Photo1']:
                    context['obj_Count_1'].Photo1 = fields['Photo1']
                context['obj_Count_1'].Content2 = fields['Content2']
                if fields['Photo2']:
                    context['obj_Count_1'].Photo2 = fields['Photo2']
                context['obj_Count_1'].Content3 = fields['Content3']
                if fields['Photo3']:
                    context['obj_Count_1'].Photo3 = fields['Photo3']
                context['obj_Count_1'].save()
            else:
                fields['Count'] = 1
                Photo_Content.objects.create(**fields)
            return redirect('image_content_admin')
        # 2.Trang Blog
        # Photo_Content.objects.filter(Count=2).delete()
        fields['Photo1'] = request.FILES.get('Photo4')
        fields['Content1'] = request.POST.get('Content4')
        fields['Photo2'] = request.FILES.get('Photo5')
        fields['Content2'] = request.POST.get('Content5')
        fields['Photo3'] = request.FILES.get('Photo6')
        fields['Content3'] = request.POST.get('Content6')
        if int(Count) == 2:
            try:
                context['obj_Count_2'] = Photo_Content.objects.get(Count=2)
            except:
                context['obj_Count_2'] = {}
            if context['obj_Count_2']:
                context['obj_Count_2'].Content1 = fields['Content1']
                if fields['Photo1']:
                    context['obj_Count_2'].Photo1 = fields['Photo1']
                context['obj_Count_2'].Content2 = fields['Content2']
                if fields['Photo2']:
                    context['obj_Count_2'].Photo2 = fields['Photo2']
                context['obj_Count_2'].Content3 = fields['Content3']
                if fields['Photo3']:
                    context['obj_Count_2'].Photo3 = fields['Photo3']
                context['obj_Count_2'].save()
            else:
                fields['Count'] = 2
                Photo_Content.objects.create(**fields)
            return redirect('image_content_admin')
        # 3.Trang Blog 1
        fields['Photo1'] = request.FILES.get('Photo7')
        fields['Content1'] = request.POST.get('Content7')
        fields['Photo2'] = request.FILES.get('Photo8')
        fields['Content2'] = request.POST.get('Content8')
        if int(Count) == 3:
            try:
                context['obj_Count_3'] = Photo_Content.objects.get(Count=3)
            except:
                context['obj_Count_3'] = {}
            if context['obj_Count_3']:
                context['obj_Count_3'].Content1 = fields['Content1']
                if fields['Photo1']:
                    context['obj_Count_3'].Photo1 = fields['Photo1']
                context['obj_Count_3'].Content2 = fields['Content2']
                if fields['Photo2']:
                    context['obj_Count_3'].Photo2 = fields['Photo2']
                context['obj_Count_3'].save()
            else:
                fields['Count'] = 3
                Photo_Content.objects.create(**fields)
            return redirect('image_content_admin')
        # 4.Trang Blog 2
        fields['Photo1'] = request.FILES.get('Photo9')
        fields['Content1'] = request.POST.get('Content9')
        fields['Photo2'] = request.FILES.get('Photo10')
        if int(Count) == 4:
            try:
                context['obj_Count_4'] = Photo_Content.objects.get(Count=4)
            except:
                context['obj_Count_4'] = {}
            if context['obj_Count_4']:
                context['obj_Count_4'].Content1 = fields['Content1']
                if fields['Photo1']:
                    context['obj_Count_4'].Photo1 = fields['Photo1']
                if fields['Photo2']:
                    context['obj_Count_4'].Photo2 = fields['Photo2']
                context['obj_Count_4'].save()
            else:
                fields['Count'] = 4
                Photo_Content.objects.create(**fields)
            return redirect('image_content_admin')
        # 5.Trang Blog 3
        fields['Photo1'] = request.FILES.get('Photo11')
        fields['Content1'] = request.POST.get('Content11')
        fields['Photo2'] = request.FILES.get('Photo12')
        fields['Photo3'] = request.FILES.get('Photo13')
        if int(Count) == 5:
            try:
                context['obj_Count_5'] = Photo_Content.objects.get(Count=5)
            except:
                context['obj_Count_5'] = {}
            if context['obj_Count_5']:
                context['obj_Count_5'].Content1 = fields['Content1']
                if fields['Photo1']:
                    context['obj_Count_5'].Photo1 = fields['Photo1']
                if fields['Photo2']:
                    context['obj_Count_5'].Photo2 = fields['Photo2']
                if fields['Photo3']:
                    context['obj_Count_5'].Photo3 = fields['Photo3']
                context['obj_Count_5'].save()
            else:
                fields['Count'] = 5
                Photo_Content.objects.create(**fields)
            return redirect('image_content_admin')
        # 5.Trang Blog 3
        fields['Photo1'] = request.FILES.get('Photo13')
        fields['Photo2'] = request.FILES.get('Photo14')
        if int(Count) == 6:
            try:
                context['obj_Count_6'] = Photo_Content.objects.get(Count=6)
            except:
                context['obj_Count_6'] = {}
            if context['obj_Count_6']:
                if fields['Photo1']:
                    context['obj_Count_6'].Photo1 = fields['Photo1']
                if fields['Photo2']:
                    context['obj_Count_6'].Photo2 = fields['Photo2']
                context['obj_Count_5'].save()
            else:
                fields['Count'] = 6   
                Photo_Content.objects.create(**fields)
            return redirect('image_content_admin')
        


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