from django.urls import path
from approoms import views

urlpatterns = [
    path('', views.index)
]
