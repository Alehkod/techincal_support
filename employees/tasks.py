from technical_support.celery import app
from .models import Employee
from django.core import serializers


@app.task
def update_paid_salary():
    for obj in Employee.objects.all():
        obj.paid_salary += obj.salary
        obj.save()
    return True


@app.task
def rm_paid_salary_celery(pk_json):
    for dict_pk in serializers.deserialize("json", pk_json, fields='pk'):
        employees = Employee.objects.filter(pk=dict_pk.object.pk)
        for obj in employees:
            obj.paid_salary = 0
            obj.save()
    return True
