from django.shortcuts import render, HttpResponse, redirect, reverse

# Create your views here.

def login(requests, status):
    # 如果用户验证成功，跳转到index页面
    # 否则留在login页面
    if status == 1:
        # 跳转
        # return redirect('/route_base/index/')
        # 反向解析带参数
        print(reverse("route_base:zoos3", args=(10,)))
        # print(reverse("route_base:zoos3"))
        return redirect(reverse('route_base:index'))
    else:
        return HttpResponse("这是login页面")


def index222(request):
    return HttpResponse("route_base index")

def index2(request):
    return render(request, 'route_base/index2.html')

def zoos(request,year,month,day):
    return HttpResponse(f"hello/{year}/{month}/{day}")

def zoos1(request, zoo_id):
    return HttpResponse(f"{zoo_id}-zoos")

def zoos2(request, id):
    return HttpResponse(f"{id}-zoos")

def zoos3(request, id, type):
    return HttpResponse(f"{id}-zoos-{type}")


# def zooname(request, name):
#     return __dict__[name](request)