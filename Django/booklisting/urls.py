from django.urls import path
from booklisting import views

urlpatterns = [
    path('', views.booklisting, name='booklisting'),
]