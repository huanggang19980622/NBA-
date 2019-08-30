from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^change_passwd/$', views.ChangePasswdView.as_view(), name='change_passwd'),
]
