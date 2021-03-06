from collections import UserList
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from .forms import *
from .models import LCL, Airfreight, Employee, Local_Air
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from employee_project.decorators import *
from users import *

###########################################################################################################
@login_required(login_url='users:login')
@staff_member_required(login_url='/main/404.html')
def FCL_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_register/FCL_list.html", context)


@login_required(login_url='users:login')
@staff_member_required(login_url='/main/404.html')
def FCL_form(request, id=0):

    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/FCL_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form = form.save(commit=False)
            user_id = request.user.pk
            form.username = User.objects.get(pk=user_id)
            form.save()
        return redirect('/main/FCL_list.html')


@login_required(login_url='users:login')
@staff_member_required(login_url='/main/404.html')
def FCL_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/main/FCL_list.html')

###########################################################################################################


@login_required(login_url='users:login')
@staff_member_required(login_url='/main/404.html')
def AIR_list(request):
    context = {'airfreight_list': Airfreight.objects.all()}
    return render(request, "employee_register/AIR_list.html", context)


@login_required(login_url='users:login')
@staff_member_required(login_url='/main/404.html')
def AIR_form(request, id=0):

    if request.method == "GET":
        if id == 0:
            form = AirfreightForm()
        else:
            airfreight = Airfreight.objects.get(pk=id)
            form = AirfreightForm(instance=airfreight)
        return render(request, "employee_register/AIR_form.html", {'form': form})
    else:
        if id == 0:
            form = AirfreightForm(request.POST)
        else:
            airfreight = Airfreight.objects.get(pk=id)
            form = AirfreightForm(request.POST, instance=airfreight)
        if form.is_valid():
            form = form.save(commit=False)
            user_id = request.user.pk
            form.username = User.objects.get(pk=user_id)
            form.save()
        return redirect('/main/AIR_list.html')


@login_required(login_url='users:login')
@staff_member_required(login_url='/main/404.html')
def AIR_delete(request, id):
    airfreight = Airfreight.objects.get(pk=id)
    airfreight.delete()
    return redirect('/main/AIR_list.html')

###########################################################################################################


@login_required(login_url='users:login')
@staff_member_required(login_url='/main/404.html')
def LCL_list(request):
    context = {'lcl_list': LCL.objects.all()}
    return render(request, "employee_register/LCL_list.html", context)


@login_required(login_url='users:login')
@staff_member_required(login_url='/main/404.html')
def LCL_form(request, id=0):
    
    if request.method == "GET":
        if id == 0:
            form = LCLForm()
        else:
            lcl = LCL.objects.get(pk=id)
            form = LCLForm(instance=lcl)
        return render(request, "employee_register/LCL_form.html", {'form': form})
    else:
        if id == 0:
            form = LCLForm(request.POST)
            
        else:
            lcl = LCL.objects.get(pk=id)
            form = LCLForm(request.POST, instance=lcl)
            
        if form.is_valid():
            form = form.save(commit=False)
            user_id = request.user.pk
            form.username = User.objects.get(pk=user_id)
            # form.LCL_origin = request.POST.get('origin')
            # form.LCL_chk_date = request.POST.get('chk_date')
            # form.LCL_dest = request.POST.get('destination')
            # form.LCL_ofc = request.POST.get('ofc')
            # form.ofcunit = request.POST.get('ofcunit')
            # form.LCL_ttime = request.POST.get('ttime')
            # form.LCL_remark = request.POST.get('remark')
            # form.LCL_effective = request.POST.get('effective')
            # form.LCL_consol = request.POST.get('consol')
            form.save()
            
            
            
        return redirect('/main/LCL_list.html')
    

@login_required(login_url='users:login')
@staff_member_required(login_url='/main/404.html')
def LCL_delete(request, id):
    lcl = LCL.objects.get(pk=id)
    lcl.delete()
    return redirect('/main/LCL_list.html')

#############################################################################################


def error(request):
    return render(request, 'employee_register/404.html')

def forgotpassword(request):
    return render(request, 'employee_register/forgot-password.html')


def index(request):
    return render(request, 'employee_register/index.html')


def register(request):
    return render(request, 'employee_register/register.html')


def search(request):
    qs = Employee.objects.all()
    q = request.GET.get('q', '')  # q??? ????????? ??? ????????? ??????

    if q:
        qs = qs.filter(dest__icontains=q) | qs.filter(origin__icontains=q) | qs.filter(
            carrier__icontains=q) 

    return render(request, 'employee_register/search.html', {
        'employee_list': qs,
        'q': q,

    })


def searchair(request):
    qs = Airfreight.objects.all()
    q = request.GET.get('q', '')  # q??? ????????? ??? ????????? ??????

    if q:
        qs = qs.filter(air_consol__icontains=q) | qs.filter(air_origin__icontains=q)\
            | qs.filter(air_dest__icontains=q)

    return render(request, 'employee_register/searchair.html', {
        'airfreight_list': qs,
        'q': q,

    })


def searchlcl(request):
    qs = LCL.objects.all()
    q = request.GET.get('q', '')  # q??? ????????? ??? ????????? ??????

    if q:
        qs = qs.filter(LCL_origin__icontains=q) | qs.filter(LCL_dest__icontains=q)\
            | qs.filter(LCL_consol__icontains=q)

    return render(request, 'employee_register/searchlcl.html', {
        'lcl_list': qs,
        'q': q,

    })

    ###################################################################################################################################

@login_required(login_url='users:login')
@staff_member_required(login_url='/main/404.html')
def Local_Air_list(request):
    context = {'Local_airfreight_list': Local_Air.objects.all()}
    return render(request, "employee_register/Local_AIR_list.html", context)


@login_required(login_url='users:login')
@staff_member_required(login_url='/main/404.html')
def Local_AIR_form(request, id=0):

    if request.method == "GET":
        if id == 0:
            form = Local_AirForm()
            
        else:
            localairfreight = Local_Air.objects.get(pk=id)
            form = Local_AirForm(instance=localairfreight)
        return render(request, "employee_register/Local_AIR_form.html", {'form': form})
    else:
        if id == 0:
            form = Local_AirForm(request.POST)
        else:
            localairfreight = Local_Air.objects.get(pk=id)
            form = Local_AirForm(request.POST, instance=localairfreight)
        if form.is_valid():
            form = form.save(commit=False)
            user_id = request.user.pk
            form.username = User.objects.get(pk=user_id)
            form.save()
        return redirect('/main/Local_AIR_list.html')


@login_required(login_url='users:login')
@staff_member_required(login_url='/main/404.html')
def Local_AIR_delete(request, id):
    localairfreight = Local_Air.objects.get(pk=id)
    localairfreight.delete()
    return redirect('/main/Local_AIR_list.html')

##############################################################
@login_required(login_url='users:login')
@staff_member_required(login_url='/main/404.html')
def Local_LCL_list(request):
    context = {'Local_lcl_list': Local_Lcl.objects.all()}
    return render(request, "employee_register/Local_LCL_list.html", context)


@login_required(login_url='users:login')
@staff_member_required(login_url='/main/404.html')
def Local_LCL_form(request, id=0):

    if request.method == "GET":
        if id == 0:
            form = Local_LclForm()
            
        else:
            locallcl = Local_Lcl.objects.get(pk=id)
            form = Local_LclForm(instance=locallcl)
        return render(request, "employee_register/Local_LCL_form.html", {'form': form})
    else:
        if id == 0:
            form = Local_LclForm(request.POST)
        else:
            locallcl = Local_Lcl.objects.get(pk=id)
            form = Local_LclForm(request.POST, instance=locallcl)
        if form.is_valid():
            form = form.save(commit=False)
            user_id = request.user.pk
            form.username = User.objects.get(pk=user_id)
            form.save()
        return redirect('/main/Local_LCL_list.html')


@login_required(login_url='users:login')
@staff_member_required(login_url='/main/404.html')
def Local_LCL_delete(request, id):
    locallcl = Local_Lcl.objects.get(pk=id)
    locallcl.delete()
    return redirect('/main/Local_LCL_list.html')