from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime,date
from TechTown.models import Employee, Department, Position, User, EmployeeAttendance,LeaveType, Leave, LeaveApproval
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

# Create your views here

@login_required
def home(request):
    emp = Employee.objects.all()
    attendance = EmployeeAttendance.objects.all()
    department = Department.objects.all()
    leave = Leave.objects.all()
    if request.method == 'POST':
        emp_id =request.POST.get('emp_id')
        start_time = request.POST.get('start_time',None)
        end_time = request.POST.get('end_time',None)
        start_time = start_time if start_time != '' else None
        end_time = end_time if end_time != '' else None
        status = request.POST.get('status')
        emp = Employee.objects.get(id=emp_id)
        EmployeeAttendance.objects.create(
            employee=emp,
            date=date.today(),
            start_time=start_time,
            end_time=end_time,
            status=status,
        )
        return redirect('/home/')
    return render(request, 'home.html',{'emp':emp,'attendance':attendance,'department':department,'leave':leave})

@login_required
def attd_del(request,attd_id):
    attd = EmployeeAttendance.objects.get(id=attd_id)
    attd.delete()
    return redirect('/home/')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/home/')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('/')

@login_required
def emp_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('ph_no')
        image = request.FILES.get('image')
        dept_id = request.POST.get('dept')
        role_id = request.POST.get('role')
        birthday = request.POST.get('bd')
        address = request.POST.get('addr')
        salary = request.POST.get('salary')
        dept = Department.objects.get(id=dept_id)
        role = Position.objects.get(id=role_id)
        emp = Employee.objects.create(
            name=name,
            email=email,
            phone=phone,
            image=image,
            dept=dept,
            role=role,
            birthday=birthday,
            address=address,
            salary=salary,
            hired_date=datetime.now()
        )
        return redirect('/emp/list/')
    else:
        role = Position.objects.all()
        dept = Department.objects.all()
        return render(request, 'emp_add.html', {'dept': dept, 'role': role})

@login_required
def emp_list(request):
    employees = Employee.objects.all()
    return render(request, 'emp_list.html', {'emp': employees})

@login_required
def emp_edit(request, emp_id):
    if request.method == 'POST':
        emp = Employee.objects.get(id=emp_id)
        emp.name = request.POST.get('name')
        emp.email = request.POST.get('email')
        emp.phone = request.POST.get('ph_no')
        emp.dept_id = request.POST.get('dept')
        emp.role_id = request.POST.get('role')
        new_image = request.FILES.get('image')
        if new_image:
            emp.image.delete(save=False)
            emp.image = new_image
        emp.birthday = request.POST.get('bd')
        emp.address = request.POST.get('addr')
        emp.salary = request.POST.get('salary')
        emp.save()
        return redirect('/emp/list/')
    if request.method == 'GET':
        emp = Employee.objects.get(id=emp_id)
        dept = Department.objects.all()
        role = Position.objects.all()
        return render(request, 'emp_edit.html', {'emp': emp, 'dept': dept, 'role': role})

@login_required
def emp_delete(request, emp_id):
    emp = Employee.objects.get(id=emp_id)
    emp.image.delete()
    emp.delete()
    return redirect('/emp/list/')

@login_required
def emp_detail(request, emp_id):
    emp = Employee.objects.get(id=emp_id)
    return render(request, 'emp_detail.html', {'emp': emp})

@login_required
def dept_and_role(request):
    if request.method == 'POST':
        if 'dname' in request.POST and 'floor' in request.POST:
            dept = Department.objects.create(
                name=request.POST.get('dname'),
                floor=request.POST.get('floor')
            )
        elif 'pname' in request.POST and 'dept' in request.POST:
            role = Position.objects.create(
                name=request.POST.get('pname'),
                department_id=request.POST.get('dept')
            )
        return redirect('/dandp/list/')
    if request.method == 'GET':
        dept = Department.objects.all()
        role = Position.objects.all()
        return render(request, 'dept_and_role.html', {'dept': dept, 'role': role})

@login_required
def dept_edit(request, dept_id):
    dept = Department.objects.get(id=dept_id)
    if request.method == 'POST':
        dept.name = request.POST.get('dname')
        dept.floor = request.POST.get('floor')
        dept.save()
        return redirect('/dandp/list/')
    else:
        dept = Department.objects.get(id=dept_id)
        return render(request, "dept_edit.html", {"dept": dept})

@login_required
def dept_del(request, dept_id):
    dept = Department.objects.get(id=dept_id)
    dept.delete()
    return redirect('/dandp/list/')

@login_required
def role_edit(request, role_id):
    role = Position.objects.get(id=role_id)
    if request.method == 'POST':
        role.name = request.POST.get('pname')
        role.department_id = request.POST.get('dept')
        role.save()
        return redirect('/dandp/list/')
    else:
        role = Position.objects.get(id=role_id)
        dept = Department.objects.all()
        return render(request, 'role_edit.html', {'role': role, 'dept': dept})

@login_required
def role_del(request, role_id):
    role = Position.objects.get(id=role_id)
    role.delete()
    return redirect('/dandp/list/')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password),
        )
        user.save()
        return redirect('/')
    else:
        emp = Employee.objects.all()
        return render(request, 'register.html', {'emp': emp})
@login_required
def leaves(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        leave_type_id =int(request.POST.get('leave_type')) 
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        reason = request.POST.get('reason')
        leave_type = LeaveType.objects.get(id=leave_type_id)
        leave = Leave.objects.create(
            employee_id=employee_id,
            leave_type=leave_type,
            start_date=start_date,
            end_date=end_date,
            reason=reason,
        )  
        return redirect('/leaves/')    
    else:
        emp = Employee.objects.all()
        leave_type = LeaveType.objects.all()
        leave = Leave.objects.all()
        return render(request,'leaves.html',{'leave':leave,'emp':emp,'leave_type':leave_type})

@login_required
def leave_approve(request,leave_id):
    leave = Leave.objects.get(id=leave_id)
    if request.method == 'POST':
        action = request.POST.get('action')
    if leave.status == 'Pending':
        if action == 'approve':
            leave.status = 'Approved'
        elif action == 'reject':
            leave.status = 'Rejected'
        else:
            return redirect('/leaves/')
        leave.save()
        LeaveApproval.objects.create(leave=leave, approved_by=request.user)
    else:
        return redirect('/leaves/')
    return redirect('/leaves/')
@login_required
def leave_detail(request,leave_id,leave_approval_id):
    leaves = Leave.objects.get(id=leave_id)
    leave_approve = LeaveApproval.objects.get(id=leave_approval_id)
    return render(request,'leave_detail.html',{'leaves':leaves,'leave_approve':leave_approve})

@login_required
def leave_delete(request,leave_id):
    leave = Leave.objects.get(id=leave_id)
    leave.delete()
    return redirect('/leaves/')

def custom_404_view(request, exception=None):
    return render(request, '404.html', status=404)
