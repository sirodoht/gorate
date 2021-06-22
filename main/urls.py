from django.urls import path

from main import views

urlpatterns = [
    path('<slug:title>/', views.rate, name="rate")
]
