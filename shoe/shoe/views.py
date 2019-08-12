from django.shortcuts import HttpResponse,render
def base(request):
    return render(request,"base.html")
