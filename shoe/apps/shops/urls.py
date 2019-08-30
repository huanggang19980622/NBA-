from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
    url(r'^list/(?P<type_id>\d+)/(?P<page>\d+)$', views.Shopslist.as_view(), name='list'),  # 列表页
    url(r'^goods/(?P<goods_id>\d+)$', views.ShopDetail.as_view(), name='detail'),
    url(r'^$', views.IndexView.as_view(), name='index'),  # 商品页作为首页
    url(r'^all/',views.Allshoes.as_view(),name='allshoes')


    # 详情页


]