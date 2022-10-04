from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('listall/', views.listall, name='listall'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete_password, name='delete'),
    path('existing', views.exist, name='existing_password')
]