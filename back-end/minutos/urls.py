from django.urls import path
from .views import home_page, privacy_page

urlpatterns = [
    path('',home_page),
    path('/privacy',privacy_page, name="privacy"),
]