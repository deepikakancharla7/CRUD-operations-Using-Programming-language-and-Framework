from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration_list, name='registration_list'),
    path('new/', views.registration_create, name='registration_new'),
    path('edit/<int:pk>/', views.registration_update, name='registration_edit'),
    path('delete/<int:pk>/', views.registration_delete, name='registration_delete'),
]
