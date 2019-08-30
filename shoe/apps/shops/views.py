from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.views.generic import View,DetailView
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
import logging
from django.http import JsonResponse
from django.core import serializers
from .models import *
import json

from apps.Home.models import User
from django.http.response import HttpResponse
from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core import serializers
from .models import *
from django.core.paginator import Paginator
# Create your views here.
class Shopslist(LoginRequiredMixin,View):
    def get(self, request, type_id, page):
        try:
            type = GoodsType.objects.get(id=type_id)
        except GoodsType.DoesNotExist:
            # 种类不存在
            return redirect(reverse('shops:index'))

        types = GoodsType.objects.all()

        # 获取排序方式  获取分类商品的信息
        # sort=default,按默认id排序; sort=price,按价格; sort=hot,按销量;
        sort = request.GET.get('sort')

        if sort == 'price':
            skus = GoodsSKU.objects.filter(type=type).order_by('price')
        elif sort == 'hot':
            skus = GoodsSKU.objects.filter(type=type).order_by('-sales')
        else:
            sort = 'default'
            skus = GoodsSKU.objects.filter(type=type).order_by('-status')  # 默认

        # 对数据进行分页
        paginator = Paginator(skus, 12)
        try:
            page = int(page)
        except Exception as e:
            page = 1

        if page > paginator.num_pages or page <= 0:
            page = 1

        # 获取第page页的Page实例对象
        skus_page = paginator.page(page)

        # todo: 进行页码的控制，页面上最多显示5个页码
        # 1. 总数不足5页，显示全部
        # 2. 如当前页是前3页，显示1-5页
        # 3. 如当前页是后3页，显示后5页
        # 4. 其他情况，显示当前页的前2页，当前页，当前页的后2页
        num_pages = paginator.num_pages
        if num_pages < 5:
            pages = range(1, num_pages)
        elif page <= 3:
            pages = range(1, 6)
        elif num_pages - page <= 2:
            pages = range(num_pages - 4, num_pages + 1)
        else:
            pages = range(page - 2, page + 3)

        # 获取新品推荐信息
        new_skus = GoodsSKU.objects.all()


        # 组织模版上下文
        context = {'type': type, 'types': types,
                   'sort': sort,
                   'skus_page': skus_page,
                   'new_skus': new_skus,
                   'pages': pages,
                   }

        return render(request, 'shop-grid-full-3-col.html', context)
class ShopDetail(LoginRequiredMixin,View):

        """详情页"""




        def get(self, request, goods_id):
                try:
                    sku = GoodsSKU.objects.get(id=goods_id)
                except GoodsSKU.DoesNotExist:
                    return redirect(reverse('shops:list'))

                # 获取商品的分类信息
                types = GoodsType.objects.all()
                goods = Goods.objects.all()
                image = GoodsImage.objects.all()


                # 获取商品的评论信息
                sku_orders = OrderGoods.objects.filter(sku=sku).exclude(comment='')

                # 获取新品推荐信息
                new_skus = GoodsSKU.objects.filter(type=sku.type).order_by('-create_time')[:2]

                # 获取同一个SPU的其他规格商品
                same_spu_skus = GoodsSKU.objects.filter(goods=sku.goods).exclude(id=goods_id)

                # 获取登录用户的额购物车中的商品的数量
                user = request.user
                cart_count = 0

                # 组织模版上下文
                context = {'sku': sku, 'types': types,
                           'sku_orders': sku_orders,
                           'new_skus': new_skus,
                           'same_spu_skus': same_spu_skus,
                           'cart_count': cart_count,
                           "goods":goods,
                           "image":image,

                           }

                return render(request, 'product-details.html', context)
class IndexView(View):
    """首页"""
    def get(self, request):
        """显示"""



        goods = Goods.objects.all()

        types = GoodsType.objects.all()
            # 获取首页轮播的商品的信息
        index_banner = IndexGoodsBanner.objects.all().order_by('index')
            # 获取首页促销的活动信息
        promotion_banner = IndexPromotionBanner.objects.all().order_by('index')

            # 获取首页分类商品信息展示
        for type in types:
                # 查询首页显示的type类型的文字商品信息
                title_banner = IndexTypeGoodsBanner.objects.filter(type=type, display_type=0).order_by('index')
                # 查询首页显示的图片商品信息
                image_banner = IndexTypeGoodsBanner.objects.filter(type=type, display_type=1).order_by('index')
                # 动态给type对象添加两个属性保存数据
                type.title_banner = title_banner
                type.image_banner = image_banner

            # 组织上下文
        context = {
                'types': types,
                'index_banner': index_banner,
                'promotion_banner': promotion_banner,
                "goods":goods
            }



        return render(request, 'index.html', context)

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
class Allshoes(LoginRequiredMixin,View):
    def get(self, request):
        types = GoodsType.objects.all()
        contact_list= GoodsSKU.objects.filter().order_by('-price')
        paginator = Paginator(contact_list, 24)  # Show 25 contacts per page

        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)
        kwgs={
                'contacts': contacts,
                'types': types,

            }

        return render(request, 'index-2.html',kwgs )





