from django.urls import path,include
from . import views
import employee_register
from employee_register.views import *

urlpatterns = [
    path('',views.index,name='index'),
    path('FCL/', views.FCL_form,name='FCL_insert'), # get and post req. for insert operation
    path('FCL/<int:id>/', views.FCL_form,name='FCL_update'), # get and post req. for update operation
    path('FCL/delete/<int:id>/',views.FCL_delete,name='FCL_delete'),
    path('FCL_list.html',views.FCL_list,name='FCL_list'),
    path('LCL/', views.LCL_form,name='LCL_insert'), # get and post req. for insert operation
    path('LCL/<int:id>/', views.LCL_form,name='LCL_update'), # get and post req. for update operation
    path('LCL/delete/<int:id>/',views.LCL_delete,name='LCL_delete'),
    path('LCL_list.html',views.LCL_list,name='LCL_list'),# get req. to retrieve and display all records
    path('AIR/', views.AIR_form, name='AIR_insert'),
    path('AIR/<int:id>/', views.AIR_form,name='AIR_update'), # get and post req. for update operation
    path('AIR/delete/<int:id>/',views.AIR_delete,name='AIR_delete'),
    path('AIR_list.html/',views.AIR_list,name='AIR_list'),
    path('404.html', views.error, name='error'),
    path('forgot-password.html', views.forgotpassword, name='forgotpassword'),
    path('index.html', views.index, name='index'),
    path('register.html', views.register, name='register'),
    path('search/',views.search, name="search"),
    path('searchair/',views.searchair, name="searchair"),
    path('searchlcl/',views.searchlcl, name="searchlcl"),

    path('Local_AIR/', views.Local_AIR_form, name='Local_AIR_insert'),
    path('Local_AIR/<int:id>/', views.Local_AIR_form,name='Local_AIR_update'), # get and post req. for update operation
    path('Local_AIR/delete/<int:id>/',views.Local_AIR_delete,name='Local_AIR_delete'),
    path('Local_AIR_list.html/',views.Local_Air_list,name='Local_AIR_list'),
    
    path('Local_LCL/', views.Local_LCL_form, name='Local_LCL_insert'),
    path('Local_LCL/<int:id>/', views.Local_LCL_form,name='Local_LCL_update'), # get and post req. for update operation
    path('Local_LCL/delete/<int:id>/',views.Local_LCL_delete,name='Local_LCL_delete'),
    path('Local_LCL_list.html/',views.Local_LCL_list,name='Local_LCL_list'),
    
    # path('Local_FCL/', views.Local_FCL_form, name='Local_FCL_insert'),
    # path('Local_FCL/<int:id>/', views.Local_FCL_form,name='Local_FCL_update'), # get and post req. for update operation
    # path('Local_FCL/delete/<int:id>/',views.Local_FCL_delete,name='Local_FCL_delete'),
    # path('Local_FCL_list.html/',views.Local_FCL_list,name='Local_FCL_list'),
    
    # path('Local_FERRY/', views.Local_FERRY_form, name='Local_FERRY_insert'),
    # path('Local_FERRY/<int:id>/', views.Local_FERRY_form,name='Local_FERRY_update'), # get and post req. for update operation
    # path('Local_FERRY/delete/<int:id>/',views.Local_FERRY_delete,name='Local_FERRY_delete'),
    # path('Local_FERRY_list.html/',views.Local_FERRYr_list,name='Local_FERRY_list'),
    
    
    
]
