from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index222, name="index3"),
    url(r'^index2/$', views.index2, name="index2"),
    # url(regex:正则, view:视图, kwgs:传递给视图的参数, name:为url/视图命名)
    # http://localhost:8000/route_base/index/
    # route_base/index/ => 跟regex匹配
    # 1. ^route_base/ => 剩下index/
    # 2. ^index/$ => 匹配上了
    # 正则匹配
    url(r'zoos/1/', views.zoos, name="zoos_id1"),
    url(r'zoos/2/', views.zoos, name="zoos_id2"),
    url(r'zoos/3/', views.zoos, name="zoos_id3"),
    url(r'zoos/\d+/', views.zoos, name="zoos"),
    # () 分组=>参数捕获(参数以位置参数方式传`递)0.，views.zoos(request,id)
    url(r'^zoos1/(\d{4})/(\d{2})/(\d{2})/$', views.zoos, name="zoos5"),
    # () 分组=>参数命名(参数以关键字参数方式传递)，views.zoos(request, id=xxx)
    url(r'zoos2/(?P<id>\d+)/', views.zoos2, name="zoos2"),
    # 第三个参数，额外传递一个参数type给视图，views.zoos3(request, id=xx , type=dog)
    url(r'zoos3/(?P<id>\d+)/', views.zoos3, {"type":"dog"} ,name="zoos3"),
    url(r'login/$', views.login, {'status':1}, name="login")
]

"""
注意：
1. 除了include包含，建议都要加$
2. 注意URL尾部/
3. 路由匹配顺序=> 执行第一条匹配上的规则
    /route_base/index/1/
    /zoos/
    /zoos/id/
"""