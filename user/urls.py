
from django.urls import path
from . import views

urlpatterns = [
    # path("", views.home, name="home_page"),
    path("register_user/", views.register, name="register"),

]
