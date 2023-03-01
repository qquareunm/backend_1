from django.urls import path
from students import views


urlpatterns = [
    path('students', views.students_handler),
    path('students/<int:pk>', views.students_handler),
]