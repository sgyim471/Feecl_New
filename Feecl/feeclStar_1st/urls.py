from django.urls import path
from django.conf.urls import url
from feeclStar_1st.views import *

urlpatterns = [
    path('', subjectList,name='list'),
    path('detail/<int:pk>/', detail_1,name='detail_1'),
    path('create/<int:pk>', create_1,name='create_1'),
    path('delete/<int:pk>/<int:pk2>', delete_1,name='delete_1'), 
    path('logout/',logout,name='logout'),
]