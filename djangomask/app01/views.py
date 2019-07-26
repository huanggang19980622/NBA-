from django.shortcuts import render,HttpResponse
from .models import UserInfo

# Create your views here.
def demo_form(request):
    msg=""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            result = UserInfo.objects.get(username=username)
            if result and result.password == password:
                return HttpResponse("welcome\t" + username)
            else:
                msg = "密码错误！"
        except:
            msg = "用户名错误！"
    kwgs = {
        "msg": msg,
    }
    return render(request,'app01/index.html',kwgs)
