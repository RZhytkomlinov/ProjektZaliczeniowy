from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.


class Employee(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class HourTableStart(models.Model):
    employee = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    day_of_shift = models.DateField(auto_now_add=True, null=True)
    start_of_shift = models.TimeField(auto_now_add=True, null=True)
    building = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.employee.name


class HourTableEnd(models.Model):
    employee = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    day_of_shift = models.DateField(auto_now_add=True, null=True)
    end_of_shift = models.TimeField(auto_now_add=True, null=True)
    building = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.employee.name
