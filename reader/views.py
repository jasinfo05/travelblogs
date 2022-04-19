from django.shortcuts import render,redirect
from blogger.models import blog
from . models import comment

def details(request):
    if request.method == 'POST':
                message=request.POST['msg']
                name=request.POST['commenter']
                imgid=request.POST['Id']
                newcomment=comment.objects.create(blogging_id=imgid,Name=name,Message=message)
                newcomment.save();

                blogobj=blog.objects.get(id=imgid)
                return render(request,'singleimage.html',{'Blog':blogobj})

    else:
        ID=request.GET['id']
        blogsobj=blog.objects.get(id=ID)   
        return render(request,'singleimage.html',{'Blog':blogsobj})

def back(request):
        return redirect('/')
    