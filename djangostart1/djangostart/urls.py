"""djangostart URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
# 导入的根路径是项目的根目录
from app01 import views

urlpatterns = [
    # 'demo/' => re.match(r'^admin/', 'demo/')
    url(r'^admin/', admin.site.urls),
    # 'demo/' => re.match(r'demo/','demo/')
    # 'demo/js/bootstrap.min.js'
    url(r'^demo/$', views.demo, name='demo'),
    url(r'^demo_form/$', views.demo_form,name='demo_form11'),
    url(r'^demo_form2/$', views.demo_form2),
    url(r'^demo_form_db/$', views.demo_form_db),
    # url包含
    url(r'^route_base/', include('apps.route_base.urls',namespace='route_base')),
    url(r'^route_resolve/', include('apps.route_resolve.urls', namespace='route_resolve')),
]
