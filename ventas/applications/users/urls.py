from django.urls import path, re_path, include
#
from . import views

app_name = 'users_app'

urlpatterns = [
    path('crear/user/api/', views.CrearUsuarioApiView.as_view(), name='crear'),
    path('login/user/api/', views.LoginView.as_view(), name='login'),
]
