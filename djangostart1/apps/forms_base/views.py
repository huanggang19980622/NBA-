from django.shortcuts import render,HttpResponse
from .forms import ContactForm

# Create your views here.
def index(request):
    contact_form = ContactForm
    return render(request,"index.html",{"form":contact_form})
