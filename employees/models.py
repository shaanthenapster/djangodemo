from django.db import models


class Employee(models.Model):
    emp_id = models.IntegerField(max_length=1000, unique=True, auto_created=True, primary_key=True)
    emp_name = models.CharField(max_length=30)
    doj = models.DateField('date of joinig')
    emp_desig = models.CharField(max_length=20)
    emp_uname = models.CharField(max_length=15)
    emp_salary = models.FloatField(max_length=10)
    emp_email = models.EmailField


class DailyWork(models.Model):
    emp_work_id = models.IntegerField(max_length=1000, unique=True, auto_created=True, primary_key=True)
    emp_refs = models.ForeignKey(Employee ,on_delete=models.CASCADE)
    work_time = models.TimeField
    work_description = models.CharField(max_length=100)
    work_remarks = models.CharField(max_length=30)

