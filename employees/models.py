from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey


class Employee(MPTTModel):
    # user = models.OneToOneField(User, related_name='login', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(verbose_name='ФИО', max_length=150, blank=True)
    position = models.CharField(verbose_name='Должность', max_length=150, blank=True)
    hire_data = models.DateTimeField(verbose_name='Дата приема на работу', null=True, blank=True)
    salary = models.DecimalField(verbose_name='Размер заработной платы', max_digits=10, decimal_places=2, null=True,
                                 blank=True)
    paid_salary = models.DecimalField(verbose_name='Информация о выплаченной зарплате', max_digits=10, decimal_places=2,
                                      null=True,
                                      blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, verbose_name='Руководитель', null=True, blank=True,
                            related_name='children')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


# Create your models here.
