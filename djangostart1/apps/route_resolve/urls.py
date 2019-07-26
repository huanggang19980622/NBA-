from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name="index3"),
    url(r'^forms_base/',include('apps.forms_base.urls',namespace="forms_base")),
]