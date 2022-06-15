from django.urls import path,include
from . import views
import employee_register
from employee_register.views import *

urlpatterns = [
    path('oceanfreight/', views.employee_form,name='employee_insert'), # get and post req. for insert operation
    path('oceanfreight/<int:id>/', views.employee_form,name='employee_update'), # get and post req. for update operation
    path('oceanfreight/delete/<int:id>/',views.employee_delete,name='employee_delete'),
    path('oceanfreight/list/',views.employee_list,name='employee_list'), # get req. to retrieve and display all records
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio_details/', views.portfolio_details, name='portfolio_details'),
    path('resume/', views.resume, name='resume'),
    path('services/', views.services, name='services'),
    path('airfreight/', views.airfreight_form, name='airfreight_insert'),
    path('airfreight/<int:id>/', views.airfreight_form,name='airfreight_update'), # get and post req. for update operation
    path('airfreight/delete/<int:id>/',views.airfreight_delete,name='airfreight_delete'),
    path('airfreight/list/',views.airfreight_list,name='airfreight_list'),
    
    
]