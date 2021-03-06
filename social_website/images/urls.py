# images/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.image_create, name='create'),
    path('like/', views.image_like, name='like'),
    path('detail/<int:id>/<slug:slug>/', views.image_detail, name='detail'),
    path('', views.image_list, name='list'),
]
