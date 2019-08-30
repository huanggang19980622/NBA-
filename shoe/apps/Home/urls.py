from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
urlpatterns=[
    url(r'^$',TemplateView.as_view(template_name="index.html"),name='base'),
    url(r'^index1/', TemplateView.as_view(template_name="index.html"), name="index1"),
    url(r'^index2/',views.index2,name="index2"),
    url(r'^index5/',views.index5,name="index5"),
    url(r'^mobile_captcha/$', views.get_mobile_captcha, name="mobile_captcha"),
    url(r'^check_captcha/$', views.check_captcha, name='check_captcha'),
    url(r'^index3/',views.index3,name="index3"),
    url(r'^index4/',views.index4,name="index4"),
    url(r'^register-login',views.Register.as_view(),name="register-login"),
    url(r'^login',views.Login.as_view(),name="login"),
    url(r'^get_captcha/$', views.get_captcha, name='get_captcha'),
    url(r'logout/$', views.logout, name="logout"),
    url(r'password/forget/$', views.PasswordForget.as_view(), name="password_forget"),
    url(r'password/reset/(\w+)/$', views.PasswordReset.as_view(), name="password_reset"),
    url(r'^shoplist/$',views.shoplist,name="shoplist"),




 ]