from django.shortcuts import render
from django.http import HttpResponse, Http404,HttpResponseRedirect
from mainsite.models import Contact,Publishing,Product,PPhoto
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from mainsite import forms
import random

#from mainsite.models import Product

def index(request):
    return render(request,'index.html', locals())

#運用djando後台建立normal user
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print("Errors", form.errors)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index/')
        else:
            return render(request, 'register.html', {'form':form})
    else:
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'register.html', context)

def contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.save()
            message = "感謝您的來信，我們已收到回饋。"
        else:
            message = "請檢查您輸入的資訊是否正確！"
    else:
        form = forms.ContactForm()
    return render(request, 'contact.html',locals())

def newbook(request):
    products = Product.objects.all()
    return render(request,'newbook.html',locals())

def detail(request,id):
	try:
		product=Product.objects.get(id = id)
		images=PPhoto.objects.filter(product=product)
	except:
		pass
	return render(request,'detail.html',locals())


