from django.shortcuts import render
from .models import blog

def index(request):
    blogobj= blog.objects.all()
    return render(request,'index.html',{'blogs':blogobj})
