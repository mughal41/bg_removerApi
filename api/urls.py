from django.contrib import admin
from django.urls import path
from .views import RemoveBg

urlpatterns = [
    path('remove/bg/', RemoveBg.as_view()),
]