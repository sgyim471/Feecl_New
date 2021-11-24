from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('search/',views.schoolList, name='schoolSearch'),
    path('logout/',views.logoutMain,name='logoutMain'),
]