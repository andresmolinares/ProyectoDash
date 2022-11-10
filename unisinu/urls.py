from django.urls import path

from unisinu import views

urlpatterns=[
    path('', views.index, name='index'),
]