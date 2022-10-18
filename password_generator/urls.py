from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.index, name='index'),
    path('create/', views.PassCreate.as_view(), name='create'),
    path('listall/', views.PasswordList.as_view(), name='listall'),
    path('detail/<int:pk>', views.PassDetail.as_view(), name='detail'),
    path('edit/<int:pk>', views.PassEdit.as_view(), name='edit'),
    path('delete/<int:pk>/', views.PassDelete.as_view(), name='delete'),
    path('existing/', views.PassExist.as_view(), name='existing_password')
]