from django.shortcuts import render
from blogger.models import blog

def details(request):
    ID=request.GET['id']
    blogsobj=blog.objects.get(id=ID)   
    return render(request,'singleimage.html',{'Blog':blogsobj})
    