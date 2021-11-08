from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from .models import Employee


class EmployeeAllSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = Employee
        fields = ['id', 'user', 'name', 'position', 'parent', 'salary', 'paid_salary', 'level', 'children']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'user', 'name', 'position', 'parent', 'salary', 'paid_salary', 'level']
