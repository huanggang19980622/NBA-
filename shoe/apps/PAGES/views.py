from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.views.generic import View,DetailView
from .models import Category
from django.contrib.auth.mixins import LoginRequiredMixin
import logging
from django.http import JsonResponse
from django.core import serializers
from .models import Category, Shop
import json

from apps.Home.models import User
from django.http.response import HttpResponse
from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core import serializers
from .models import *
# Create your views here.
class Shoplist(LoginRequiredMixin,View):
    def get(self,request):
        category = Category.objects.all().values("id","name")
        shoes = Shop.DIF_CHOICES
        search = request.GET.get("search","")
        shops = Shop.objects.all()
        tag = Tag.objects.all()
        kwgs = { "category":category,
                 "shoes":shoes,
                 "search_key":search,
                 'shops': shops,
                 "tag":tag,

        }
        return render(request,'shop-grid-full-4-col.html',kwgs)
