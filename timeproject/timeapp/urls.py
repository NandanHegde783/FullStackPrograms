from . import views
from django.urls import path

urlpatterns = [
    path('time/', views.current_datetime, name = 'current_datetime'),
]