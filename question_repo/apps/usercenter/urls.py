from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # 个人资料
    url(r'^profile/$', TemplateView.as_view(template_name="uc_profile.html"), name='profile'),
    # 修改密码
    url(r'^change_passwd/$', views.test, name='change_passwd'),
    #　我的回答
    url(r'^answer/$', views.test, name='answer'),
    # 我的收藏
    url(r'^collect/$', views.test, name='collect'),
    # 我的贡献
    url(r'^contribut/$', views.test, name='contribut'),
    # 待审题目
    url(r'^approval/$', views.test, name='approval'),
    # 审核题目
    url(r'^approval/id/$', views.test, name='approval_pass'),
]