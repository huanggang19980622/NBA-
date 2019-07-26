from django.shortcuts import render,HttpResponse
from .models import UserInfo

# Create your views here.
def demo(request):
    return render(request,'app01/demo01.html')
def demo_form(request):
	msg = ""
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		UserInfo.objects.create(username=username,password=password)
		user_list = UserInfo.objects.all()

		result = UserInfo.objects.get(username=username)
		if result and result.password == password:
			return render(request,'app01/success.html',{"user_list":user_list})
		else:
			msg="密码错误！"

	kwgs = {
		"msg":msg
	}
	return render(request, 'app01/demo02_form.html',kwgs)
