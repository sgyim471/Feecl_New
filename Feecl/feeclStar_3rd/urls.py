from django.urls import path
from django.conf.urls import url
from feeclStar_3rd.views import *

urlpatterns = [
    path('', subjectList,name='list'),
    path('detail/<int:pk>/', detail_3,name='detail_3'),
    path('create/<int:pk>', create_3,name='create_3'),
    path('delete/<int:pk>/<int:pk2>', delete_3,name='delete_3'), 
    path('logout/',logout,name='logout'),
]