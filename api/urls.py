from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("api/data/", views.api_data, name="api_data"),
    path("api/user/", views.user_data, name="user_data"),
]

