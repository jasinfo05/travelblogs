from django.shortcuts import render,redirect
from .models import blog
from django.http.response import JsonResponse

def index(request):
    if request.method=='POST':
        data=request.POST['searchdata']
        images=blog.objects.filter(name__istartswith=data)
        return render(request,'index.html',{'blogs':images})

    else:
        blogobj= blog.objects.all()
        return render(request,'index.html',{'blogs':blogobj})

def searchitem(request):
    if 'item' in request.GET:
        letter=request.GET['item']
        print(letter)
        list1=[]
        imgobj=blog.objects.filter(name__istartswith=letter)
        print(imgobj)
        for items in imgobj:
            list1.append(items.name)
            print(list1)
        return JsonResponse(list1,safe=False)
    return redirect('/')