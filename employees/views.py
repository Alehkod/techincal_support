from rest_framework.generics import ListAPIView
from rest_framework import filters
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeesList(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['level']
