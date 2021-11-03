from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey


class Employee(MPTTModel):
    user = models.OneToOneField(User, related_name='login', on_delete=models.CASCADE, null=True, blank=True)
    patronymic = models.CharField('Отчество', max_length=20, blank=True)
    position = models.CharField('Должность', max_length=20, blank=True)
    hire_data = models.DateTimeField('Дата приема на работу', null=True, blank=True)
    salary = models.DecimalField('Размер заработной платы', max_digits=6, decimal_places=2, null=True, blank=True)
    paid_salary = models.DecimalField('Информация о выплаченной зарплате', max_digits=6, decimal_places=2, null=True,
                                      blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return f'{self.user}'

# Create your models here.
