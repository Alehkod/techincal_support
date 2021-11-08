from rest_framework import generics
from rest_framework import filters
from .models import Employee
from .serializers import EmployeeSerializer, EmployeeAllSerializer
from rest_framework.permissions import IsAuthenticated


class EmployeesList(generics.ListAPIView):
    """Generic API of all employees"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeAllSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['level']


class EmployeesListLevel(generics.ListAPIView):
    """Generic API of employees by level"""
    def get_queryset(self):
        level = self.kwargs['level']
        return Employee.objects.filter(level=level)

    serializer_class = EmployeeSerializer


class EmployeeView(generics.ListAPIView):
    """Generic API current employees"""
    def get_queryset(self):
        employee = self.request.user
        return Employee.objects.filter(user=employee)
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated, ]
