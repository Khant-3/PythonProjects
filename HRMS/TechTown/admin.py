from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from TechTown.models import Employee, Department, Position, Leave, User,LeaveType,LeaveApproval,EmployeeAttendance
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User

admin.site.register(User,CustomUserAdmin)

admin.site.register(Employee)

admin.site.register(EmployeeAttendance)

admin.site.register(Department)

admin.site.register(Position)

admin.site.register(Leave)

admin.site.register(LeaveType)

admin.site.register(LeaveApproval)

