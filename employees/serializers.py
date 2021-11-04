from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = Employee
        fields = '__all__'
