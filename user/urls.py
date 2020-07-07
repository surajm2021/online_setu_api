from django.urls import path
from . import views

urlpatterns = [
    path("register_user/", views.register, name="register"),
    path("login_user/", views.login_user, name="login_user"),
    path('logout_user/', views.logout, name='logout'),
    path('profile_user/', views.profileinfo, name='profile'),
    path('login_user_by_otp/', views.verify_opt, name='verify_otp'),
    path('password_change/', views.password_change, name='password_change'),
    path('mobile_no_change/', views.mobile_no_change, name='mobile_no_change'),
]
