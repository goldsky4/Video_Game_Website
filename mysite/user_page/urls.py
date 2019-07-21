from django.urls import path
from . import views

urlpatterns = [
    path('', views.user),
    path('create_account/', views.createuser),
    path('logout/', views.log_out),
    path('test/', views.test),
]
