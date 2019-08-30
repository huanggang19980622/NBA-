"""shoe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls import url, include
from django.views.static import serve
from .settings import MEDIA_ROOT
from . import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # #
    url(r'^apis/',include('apps.Apis.urls',namespace="Apis")),
    # url(r'^PAGES/',include('apps.PAGES.urls',namespace="PAGES")),
    # url(r'^SHOP/',include('apps.SHOP.urls',namespace="SHOP")),
    # url(r'^CONTACTUS/',include('apps.CONTACTUS.urls',namespace="CONTACTUS")),
    url(r'^user',include('apps.Home.urls',namespace="Home")),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # ckeditor
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^pages/', include('apps.PAGES.urls', namespace='pages')),

    url(r'^uc/', include('apps.Usercenter.urls', namespace='Uc')),
    url(r'^',include('apps.shops.urls',namespace="shops")),
    url(r'^search/', include('haystack.urls')),  # 全文检索框架








]