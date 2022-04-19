from unicodedata import name
from django.urls import URLPattern, path
from . import views

urlpatterns =[
    path('reader',views.details,name="details"),
    path('home',views.back,name="backpage")
]