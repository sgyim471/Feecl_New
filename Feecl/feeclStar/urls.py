from django.urls import path
from django.conf.urls import url
from feeclStar.views import *

urlpatterns = [
    path('', subjectList,name='list'),
    path('detail/<int:pk>/', detail,name='detail'),
    path('create/<int:pk>', create,name='create'),
    path('delete/<int:pk>/<int:pk2>', delete,name='delete'), 
    path('logout/',logout,name='logout'),
]

