from django.shortcuts import render, redirect
from .forms import AirfreightForm, EmployeeForm
from .models import Airfreight, Employee


###########################################################################################################
def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)


def employee_form(request, id=0):
    
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance= employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/main/oceanfreight/list')


def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/main/oceanfreight/list')

###########################################################################################################

def airfreight_list(request):
    context = {'airfreight_list': Airfreight.objects.all()}
    return render(request, "employee_register/airfreight_list.html", context)

def airfreight_form(request, id=0):
    
    if request.method == "GET":
        if id == 0:
            form = AirfreightForm()
        else:
            airfreight = Airfreight.objects.get(pk=id)
            form = AirfreightForm(instance= airfreight)
        return render(request, "employee_register/airfreight_form.html", {'form': form})
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



def about(request):
    return render(request, 'employee_register/about.html')

def contact(request):
    return render(request, 'employee_register/contact.html')

def portfolio(request):
    return render(request, 'employee_register/portfolio.html')

def portfolio_details(request):
    return render(request, 'employee_register/portfolio-details.html')

def resume(request):
    return render(request, 'employee_register/resume.html')

def services(request):
    return render(request, 'employee_register/services.html')