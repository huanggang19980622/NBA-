from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.views.generic import View,DetailView
from .models import Category,Questions
from django.contrib.auth.mixins import LoginRequiredMixin
import logging
from django.http import JsonResponse
from django.core import serializers
from .models import Category, Questions, Answers
import json
from .models import UserLog

logger = logging.getLogger("repo")


# Create your views here.
def test(request):
    return HttpResponse("题库视图")
class QuestionsList(View,LoginRequiredMixin):
    def get(self, request):
        category = Category.objects.all().values("id", "name")
        grades = Questions.DIF_CHOICES
        search = request.GET.get("search", "")
        kwgs = {"category": category,
                "grades": grades,
                "search_key": search
                }
        # kwgs = {"category": category, "grades": grades}
        return render(request, 'question.html', kwgs)

from django.db import transaction
class QuestionDetail(DetailView):
    model = Questions
    pk_url_kwarg = 'id'
    template_name = "question_detail.html"
    # 默认名：object
    context_object_name = "object"

    def get_context_data(self, **kwargs):
        # kwargs：字典、字典中的数据返回给html页面
        # self.get_object() => 获取当前id的数据（问题）
        question = self.get_object()  # 当前这道题目
        kwargs["my_answer"] = Answers.objects.filter(question=question, user=self.request.user)
        return super().get_context_data(**kwargs)

    def post(self, request, id):
        try:
            with transaction.atomic():
                # data_answer: 用户提交的数据
                data_answer = request.POST.get('answer', "没有回答")
                new_answer = Answers.objects.get_or_create(question=self.get_object(), user=request.user)
                new_answer[0].answer = data_answer
                new_answer[0].save()
                my_answer = json.loads(serializers.serialize("json", [new_answer[0]]))[0]
                # OPERATE = ((1, "收藏"), (2, "取消收藏"), (3, "回答"))
                # raise  TypeError
                UserLog.objects.create(user=request.user, operate=3, question=self.get_object(), answer=new_answer[0])
                result = {'status': 1, 'msg': '提交成功', 'my_answer': my_answer}
                return JsonResponse(result)
        except Exception as ex:
            logger.error(ex)
            my_answer = {}
            msg = "提交失败"
            code = 500

        result = {"status": code, "msg": msg, "my_answer": my_answer}
        return JsonResponse(result)





        # return HttpResponse('abc')


# 要求用户需要登录了才能访问该页面，如果没有登录，跳转到。=> '/accounts/login/'
@login_required
def index(request):
    return render(request, "index.html")

#
@login_required
def questions(request):
      category = Category.objects.all()
      grades = Questions.DIF_CHOICES
      search = request.GET.get("search","")
      kwgs = {"category":category,
              "grades":grades,
              "search_key":search
              }
      return  render(request, "question.html", kwgs)