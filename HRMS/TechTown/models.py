from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
# Create your models here.


class User(AbstractUser):
    employee = models.OneToOneField(
        'Employee', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username


class Department(models.Model):
    name = models.CharField(max_length=30, null=False)
    floor = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=40, null=False)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Employee(models.Model):
    image = models.ImageField(blank=True)
    name = models.CharField(max_length=40)
    dept = models.ForeignKey('Department', on_delete=models.CASCADE)
    role = models.ForeignKey('Position', on_delete=models.CASCADE)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=30)
    birthday = models.DateField()
    address = models.TextField()
    salary = models.IntegerField()
    hired_date = models.DateField()

    def __str__(self):
        return self.name


class EmployeeAttendance(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    start_time = models.TimeField(blank=True,null=True)
    end_time = models.TimeField(blank=True,null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.employee.name}'s Daily Report - {self.date}"

class LeaveType(models.Model):
    leave_type = models.CharField(max_length=40)

    def __str__(self):
        return self.leave_type

class Leave(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    leave_type = models.ForeignKey('LeaveType',on_delete=models.CASCADE,default='Personal Leave')
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=40,default='Pending')

    def __str__(self):
        return f"{self.employee.name}'s Leave"


class LeaveApproval(models.Model):
    leave = models.ForeignKey('Leave', on_delete=models.CASCADE)
    approved_by = models.ForeignKey('User', on_delete=models.CASCADE)
    approval_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.leave.employee.name}'s Leave Approval by {self.approved_by.username} on {self.approval_date}"
