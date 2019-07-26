from django.shortcuts import render, HttpResponse
from .models import UserInfo


# Create your views here.

# django 会给视图传一个参数（HttpRequest）
def demo(request):
    """最简单的html页面"""
    # 返回一个HttpResponse对象
    # return HttpResponse('HelloWorld')
    # request, html模板, 传递到html页面的信息
    return render(request, 'app01/demo01.html')


def demo_form(request):
    """表单提交"""
    # print(request.GET)
    # username = request.GET["email"]       # key
    username = request.GET.get("email")       # key
    password = request.GET.get("password")   # get => 当key不存在

    # 返回一个HttpResponse对象
    # return HttpResponse('HelloWorld')
    # request, html模板, 传递到html页面的信息=> 字典格式
    return render(request, 'app01/demo02_form.html', {"user":username})


def demo_form2(request):
    """
    表单post提交，并验证用户登录
    """
    userlist = {"a@a.com":"123123"}
    # 验证用户登录，如果验证成功，跳转到欢迎您，否则跳转到登录页面
    msg = ""
    if request.method == "POST":
        username = request.POST.get("email")       # key
        password = request.POST.get("password")   # get => 当key不存在
        if username in userlist and password == userlist[username]:
            return HttpResponse(f"<h2>欢迎您，{username}</h2>")
        else:
            msg = "用户名或密码错误！"
    # 返回一个HttpResponse对象
    # return HttpResponse('HelloWorld')
    # request, html模板, 传递到html页面的信息=> 字典格式
    kwgs = {
        "msg":msg,
    }
    return render(request, 'app01/demo02_form2.html', kwgs)



def demo_form_db(request):
    """
    表单post提交，并验证用户登录
    """
    # 从数据中查找所有的用户信息，放到userlist => querySet
    # queryset[UserInfoojbect, UserInfoojbect,]
    # userlist = UserInfo.objects.all()
    # 验证用户登录，如果验证成功，跳转到欢迎您，否则跳转到登录页面
    msg = ""
    if request.method == "POST":
        username = request.POST.get("email")       # key
        password = request.POST.get("password")   # get => 当key不存在
        # try...except...
        try:
            result = UserInfo.objects.get(email=username)
            # xxx.objects.get =>  取一个，如果数据中有0个或多个都会抛出错误
            # xxx.objects.filter => 取0个或n个 => 不出抛出错误
            # select * from userinfo where email=“aaa"
            if result.password == password:
                return HttpResponse(f"<h2>欢迎您，{username}</h2>")
            else:
                msg = "用户名或密码错误！"
        except Exception as ex:
            msg = "用户不存在！"
    # 返回一个HttpResponse对象
    # return HttpResponse('HelloWorld')
    # request, html模板, 传递到html页面的信息=> 字典格式
    kwgs = {
        "msg":msg,
    }
    return render(request, 'app01/demo02_form_db.html', kwgs)
