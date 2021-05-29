from django.urls import path
from .views import home_page, privacy_page, plans_page

urlpatterns = [
    path('',home_page),
    path('/privacy', privacy_page, name="privacy"),
    path('/plans', plans_page, name="plans"),
]