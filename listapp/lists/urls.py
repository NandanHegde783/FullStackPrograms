from django.urls import path
from . import views
urlpatterns = [
    path('fruit_list/', views.fruit_list, name = 'fruit_list'),
    path('student_list/', views.student_list, name ='student_list'),
]