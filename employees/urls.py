from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'employees'
urlpatterns = [
    path('employees', views.EmployeesList.as_view(), name='employees_list'),
    path('employees/<int:level>/', views.EmployeesListLevel.as_view()),
    path('profile', views.EmployeeView.as_view(), name='employee'),
]
