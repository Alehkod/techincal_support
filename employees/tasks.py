from technical_support.celery import app
from .models import Employee


@app.task
def update_paid_salary():
    for obj in Employee.objects.all():
        obj.paid_salary += obj.salary
        obj.save()
    return True
