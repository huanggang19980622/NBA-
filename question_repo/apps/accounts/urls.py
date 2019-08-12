from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

# CBV => class base view
# FBV => function base view

urlpatterns = [
    # 注册
    url(r'register/$', views.Register.as_view(), name="register"),
    # 登录
    url(r'^login/$', views.Login.as_view(), name='login'),
    # 退出
    url(r'logout/$', views.logout, name="logout"),
    # 忘记密码
    url(r'password/forget/$', views.test, name="password_forget"),
    # 重置密码
    url(r'password/reset/token/$',views.test, name="password_reset"),
]