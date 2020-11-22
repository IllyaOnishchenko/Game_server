from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path("registration/", views.register, name = "register"),
    path("login/", views.login, name = "login")
]