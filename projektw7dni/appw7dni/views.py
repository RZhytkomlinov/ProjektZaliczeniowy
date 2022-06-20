from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# Create your views here.
from .models import *
from .forms import EmpForm, CreateUserForm, StartTime, EndTime
from .decorators import unauthenticated_user, allowed_users, admin_only
import datetime


@login_required(login_url='login')
@admin_only
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@admin_only
def home(request):
    employees = Employee.objects.all()

    context = {'employees': employees}

    return render(request, 'home.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['employee'])
def home_employee(request):
    current_employee = User.objects.get(username=request.user)
    name = current_employee.employee
    start = current_employee.employee.hourtablestart_set.all()
    end = current_employee.employee.hourtableend_set.all()

    startform = StartTime()
    endform = EndTime()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        if 'starttime' in request.POST:
            form = StartTime(request.POST)
            if form.is_valid():
                f_form = form.save(commit=False)
                f_form.employee = name
                f_form.save()
                return redirect('home_employee')
        elif 'endtime' in request.POST:
            form = EndTime(request.POST)
            if form.is_valid():
                f_form = form.save(commit=False)
                f_form.employee = name
                f_form.save()
                return redirect('home_employee')

    context = {'start': start, 'name': name, 'end': end, 'startform': startform, 'endform': endform}
    return render(request, 'home_emp.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def hour_table(request, pk):
    employee = Employee.objects.get(id=pk)
    start = HourTableStart.objects.filter(employee_id=pk)
    end = HourTableEnd.objects.filter(employee_id=pk)
    context = {'employee': employee, 'start': start, 'end': end}

    return render(request, 'hour_table.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def create_employee(request):
    form = EmpForm()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = EmpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../')

    context = {'form': form}
    return render(request, 'create_emp.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmpForm(instance=employee)

    if request.method == 'POST':
        form = EmpForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'create_emp.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == "POST":
        employee.delete()
        return redirect('home')

    context = {'employee': employee}
    return render(request, 'delete_emp.html', context)
