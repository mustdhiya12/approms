from django.urls import path
from learningOnline import views

urlpatterns = [
    path('', views.index)
]
