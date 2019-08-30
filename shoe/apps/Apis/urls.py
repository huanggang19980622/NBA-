from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
urlpatterns=[
    url(r'^blog_details/$',views.blog_details,name="blog_details"),
    url(r'^blog_audio/$',views.blog_audio,name="blog_audio"),
    url(r'^blog_details_image/$',views.blog_details_image,name="blog-details-image"),
    url(r'^change_avator/$', views.ChangeAvator.as_view(), name='change_avator'),
    url(r'^shoes/$', views.ShoesView.as_view(), name='shoes'),
]