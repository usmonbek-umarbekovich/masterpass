from django.urls import path
from . import views
from .views import PassCreate, PassDelete, PassDetail, PassEdit, PassExist, PasswordList

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', PassCreate.as_view(), name='create'),
    path('listall/', PasswordList.as_view(), name='listall'),
    path('detail/<int:pk>', PassDetail.as_view(), name='detail'),
    path('edit/<int:pk>', PassEdit.as_view(), name='edit'),
    path('delete/<int:pk>/', PassDelete.as_view(), name='delete'),
    path('existing', PassExist.as_view(), name='existing_password')
]