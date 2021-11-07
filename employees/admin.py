from django.contrib import admin
from .models import *

from django.urls import reverse
from django.utils.html import format_html


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'link_to_parent', 'salary', 'paid_salary')
    list_display_links = ('name', 'link_to_parent')
    list_filter = ('position', 'level')
    search_fields = ('name', 'position')

    # Remove all information about the paid salaries of all selected employees
    @admin.action(description='Удалить инофрмацию о выплаченной зарплате')
    def rm_paid_salary(self, request, queryset):
        queryset.update(paid_salary=0)

    actions = [rm_paid_salary]

    def link_to_parent(self, obj):
        link = reverse("admin:employees_employee_change", args=[obj.parent_id])
        return format_html('<a href="{}"> {}</a>', link, obj.parent)

    link_to_parent.short_description = 'Руководитель'

# Register your models here.
