from django.urls import path
from feeclBoard import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index_board, name='index_board'),
    path('post/', views.post, name='post'),
    path('post/<int:id>/', views.detail_board, name='detail_board'),
    path('post/commentNew/<int:pk>',views.comment_write, name='comment_new' ),
    path('post/edit/<int:pk>/', views.to_update_board, name='to_update_board'),
    path('post/edit/upload/<int:pk>/', views.update_board, name='update_board'), 
    path('post/delete/<int:pk>/',views.delete_board, name='delete_board'),
    path('post/delete/<int:pk>/<int:pk2>', views.delete_comment,name='delete_comment'),
    path('logout/',views.logout ,name='logout'),
]
