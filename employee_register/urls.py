from django.urls import path,include
from . import views
import employee_register
from employee_register.views import *

urlpatterns = [
    path('',views.index,name='index'),
    path('FCL/', views.FCL_form,name='FCL_insert'), # get and post req. for insert operation
    path('FCL/<int:id>/', views.FCL_form,name='FCL_update'), # get and post req. for update operation
    path('FCL/delete/<int:id>/',views.FCL_delete,name='FCL_delete'),
    path('FCL_list.html',views.FCL_list,name='FCL_list'), # get req. to retrieve and display all records
    path('airfreight/', views.airfreight_form, name='airfreight_insert'),
    path('airfreight/<int:id>/', views.airfreight_form,name='airfreight_update'), # get and post req. for update operation
    path('airfreight/delete/<int:id>/',views.airfreight_delete,name='airfreight_delete'),
    path('airfreight/list/',views.airfreight_list,name='airfreight_list'),
    path('404.html', views.error, name='error'),
    path('blank.html', views.blank, name='blank'),
    path('buttons.html', views.buttons, name='buttons'),
    path('cards.html', views.cards, name='cards'),
    path('charts.html', views.charts, name='charts'),
    path('forgot-password.html', views.forgotpassword, name='forgotpassword'),
    path('index.html', views.index, name='index'),
    path('login.html', views.login, name='login'),
    path('register.html', views.register, name='register'),
    path('table.html', views.table, name='table'),
    path('utilities-animation.html', views.utilitiesanimation, name='utilitiesanimation'),
    path('utilities-border.html', views.utilitiesborder, name='utilitieborder'),
    path('utilities-color.html', views.utilitiescolor, name='utilitiescolor'),
    path('utilities-other.html', views.utilitiesother, name='utilitiesother'),
    path('search/',views.search, name="search"),
    
    
    
    
    
]
