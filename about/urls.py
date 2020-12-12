from django.urls import path

from . import views


urlpatterns = [
    path('', views.main_about, name='main_about'),
]