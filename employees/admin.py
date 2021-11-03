from django.contrib import admin
from .models import *


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'parent', 'salary', 'paid_salary')
    list_display_links = ('name', 'parent')
    list_filter = ('position', 'level')
    search_fields = ('name', 'position')

    # Remove all information about the paid salaries of all selected employees
    @admin.action(description='Удалить инофрмацию о выплаченной зарплате')
    def rm_paid_salary(self, request, queryset):
        queryset.update(paid_salary=0)

    actions = [rm_paid_salary]

# Register your models here.
