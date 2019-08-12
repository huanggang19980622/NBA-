from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
    url(r'^$', views.index, name='index'),

    # 题目列表
    url(r'^questions/$', TemplateView.as_view(template_name="questions.html"), name="questions"),
    # 贡献题目
    url(r'^question/$', views.questions, name="question"),
    # 题目详情，捕获了一个参数
    url(r'^question/(?P<id>\d+)/$',views.QuestionDetail.as_view(), name="question_detail"),

]