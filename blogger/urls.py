from django.urls import URLPattern, path
from . import views

urlpatterns =[
    path('',views.index,name="indexpage"),
    path('search/',views.searchitem,name="searchinfo"),
]