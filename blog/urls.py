from django.urls import path

from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('device/add/', views.device_add, name='device_add'),
    path('device/', views.device, name='device'),
    path('device/start/', views.device_start, name='device_start'),
    path('device/stop/', views.device_stop, name='device_stop')
]