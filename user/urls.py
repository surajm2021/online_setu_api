
from django.urls import path
from . import views

urlpatterns = [
    # path("", views.home, name="home_page"),
    path("register_user/", views.register, name="register"),
    path("login_user/", views.login_user, name="login_user"),
    path('logout_user/', views.logout, name='logout'),
    path('profile_user/', views.profileinfo, name='profile'),
    path('login_user_by_otp/', views.verify_opt, name='verifyotp'),
]
