from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.generic import View

# Create your views here.
def blog_details(request):
    return render(request,"blog-details.html")
def blog_audio(request):
    return render(request,"blog-details-audio.html")
def blog_details_image(request):
    return render(request,"blog-details-image.html")


import base64
import os
import time
import datetime
from shoe.settings import MEDIA_ROOT, MEDIA_URL


class ChangeAvator(LoginRequiredMixin, View):
    def post(self, request):
        today = datetime.date.today().strftime("%Y%m%d")
        # 图片的data-img格式=>data:image/jpg;base64,xxxx
        img_src_str = request.POST.get("image")
        img_str = img_src_str.split(',')[1]
        # 取出格式:jpg/png...
        img_type = img_src_str.split(';')[0].split('/')[1]
        # 取出数据:转化为bytes格式
        img_data = base64.b64decode(img_str)
        # 相对上传路径: 头像上传的相对路径
        avator_path = os.path.join("avator", today)
        # 绝对上传路径：头像上传的绝对路径
        avator_path_full = os.path.join(MEDIA_ROOT, avator_path)
        if not os.path.exists(avator_path_full):
            os.mkdir(avator_path_full)
        filename = str(time.time()) + "." + img_type
        # 绝对文件路径，用于保存图片
        filename_full = os.path.join(avator_path_full, filename)
        # 相对MEDIA_URL路径，用于展示数据
        img_url = f"{MEDIA_URL}{avator_path}/{filename}"
        try:
            with open(filename_full, 'wb') as fp:
                fp.write(img_data)
            ret = {
                "result": "ok",
                "file": img_url
            }
        except Exception as ex:
            ret = {
                "result": "error",
                "file": "upload fail"
            }

        request.user.avator_sor = os.path.join(avator_path, filename)
        request.user.save()
        return JsonResponse(ret)


from django.http import JsonResponse
from django.views.generic import View
from apps.PAGES.models import Shop

from django.db.models import Q
class ShoesView(View):
    def get(self, request):
        """
        :param request:
        :return:
        # /apis/questions/?order=asc&offset=0&limit=25
        # /apis/questions/?pagesize=25&offset=0&page=1&grade=4&category=1&status=1
        """
        # 获取参数
        page = int(request.GET.get("page", 1))
        pagesize = int(request.GET.get("pagesize", 25))
        offset = int(request.GET.get("offset", 0))
        grade = int(request.GET.get("shoes", 0))
        category = int(request.GET.get("category", 0))
        # 2: 不筛选， 1，已刷，0，待刷
        status = int(request.GET.get("status", 0))
        search = request.GET.get("search", "")

        # 取出所有数据，筛选指定等级和分类
        questions_list = Shop.objects.filter(status=1)
        # if search:
        #     questions_list = questions_list.filter(title__icontains=search)

        if search:
            if search.isdigit():
                questions_list = questions_list.filter(
                    Q(id=search) | Q(content__icontains=search) | Q(title__icontains=search))
            else:
                questions_list = questions_list.filter(Q(content__icontains=search) | Q(title__icontains=search))

        if grade: questions_list = questions_list.filter(shoes=grade)
        if category: questions_list = questions_list.filter(category__id=category)

        # 筛选状态 => 我的答题表
        questions_list = questions_list.values('id', 'title', 'shoes', 'content')
        total = len(questions_list)

        # 计算当前页面的数据
        questions_list = questions_list[offset:offset + pagesize]

        # 用于计算当前登录的用户是否收藏对应的题目，如果收藏实心True，没有收藏空心False
        for item in questions_list:
            item["collection"] = True if Shop.objects.filter(
                user=request.user, status=True, question_id=item["id"]) else False

        # 格式是bootstrap-table要求的格式
        questions_dict = {'total': total, 'rows': list(questions_list)}
        return JsonResponse(questions_dict, safe=False)