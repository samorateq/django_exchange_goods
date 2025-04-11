from django.urls import path
from users import views


app_name = 'user'

urlpatterns = [
    path('login/', views.log_in, name='login'),
    path('register/', views.register_user, name='register'),
    path('profile/', views.profile_user, name='profile'),
    path('logout/', views.logout_user, name='logout'),
]