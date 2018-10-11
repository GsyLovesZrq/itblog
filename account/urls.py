from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

app_name = "account"

urlpatterns = [
    #path('login/', views.user_login, name='user_login'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html', next_page='/blog/'),
         name='user_logout'),
    path('register/', views.register, name='user_register'),
    path('password_change/', auth_views.PasswordChangeView.as_view(success_url='/account/password_change_done'),
         name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('information/', views.myself, name='information'),
    path('edit_information/', views.myself_edit, name='edit_my_information'),
    path('my-image', views.my_image, name='my_image'),
]