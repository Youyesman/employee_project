from django.shortcuts import render, redirect
from .forms import AirfreightForm, EmployeeForm
from .models import Airfreight, Employee
from django.db.models import Q


###########################################################################################################
def FCL_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_register/FCL_list.html", context)


def FCL_form(request, id=0):
    
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance= employee)
        return render(request, "employee_register/FCL_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/main/FCL_list.html')


def FCL_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/main/FCL_list.html')

###########################################################################################################

def airfreight_list(request):
    context = {'airfreight_list': Airfreight.objects.all()}
    return render(request, "employee_register/AIR_list.html", context)

def airfreight_form(request, id=0):
    
    if request.method == "GET":
        if id == 0:
            form = AirfreightForm()
        else:
            airfreight = Airfreight.objects.get(pk=id)
            form = AirfreightForm(instance= airfreight)
        return render(request, "employee_register/AIR_form.html", {'form': form})
    else:
        if id == 0:
            form = AirfreightForm(request.POST)
        else:
            airfreight = Airfreight.objects.get(pk=id)
            form = AirfreightForm(request.POST,instance= airfreight)
        if form.is_valid():
            form.save()
        return redirect('/main/airfreight/list')


def airfreight_delete(request,id):
    airfreight = Airfreight.objects.get(pk=id)
    airfreight.delete()
    return redirect('/main/airfreight/list')


###########################################################################################################

def error(request):
    return render(request, 'employee_register/404.html')

def blank(request):
    return render(request, 'employee_register/blank.html')

def buttons(request):
    return render(request, 'employee_register/buttons.html')

def cards(request):
    return render(request, 'employee_register/cards.html')

def charts(request):
    return render(request, 'employee_register/charts.html')

def forgotpassword(request):
    return render(request, 'employee_register/forgot-password.html')

def index(request):
    return render(request, 'employee_register/index.html')

def login(request):
    return render(request, 'employee_register/login.html')

def register(request):
    return render(request, 'employee_register/register.html')

def table(request):
    return render(request, 'employee_register/table.html')

def utilitiesanimation(request):
    return render(request, 'employee_register/utilities-animation.html')

def utilitiesborder(request):
    return render(request, 'employee_register/utilities-border.html')

def utilitiescolor(request):
    return render(request, 'employee_register/utilities-color.html')

def utilitiesother(request):
    return render(request, 'employee_register/utilities-other.html')

def search(request):
    qs = Employee.objects.all()
    q = request.GET.get('q', '') # q가 없으면 빈 문자열 리턴

    if q:
        qs = qs.filter(dest__icontains=q)|qs.filter(origin__icontains=q)|qs.filter(carrier__icontains=q)|qs.filter(position__icontains=q)

    return render(request, 'employee_register/search.html', {
        'employee_list': qs,
        'q': q,
 
    })