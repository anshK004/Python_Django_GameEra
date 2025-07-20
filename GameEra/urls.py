"""
URL configuration for GameEra project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from development import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name="home.html"),
    path("homepage",views.homepage),
    path("loginlink",views.login),
    path("aboutus",views.aboutus),
    path("signup",views.signup),
    path("contactus",views.contactus),
    path("mall",views.mall),
    path("customer",views.customer),
    path("AdminHome",views.AdminHome),
    path("CustomerHome",views.CustomerHome),
    path("AdminEmail",views.AdminEmail),
    path("AdminContact",views.AdminContact),
    path("AdminAddress",views.AdminAddress),
    path("AccountCreation",views.AccountCreation),
    path("AdminPassword",views.AdminPassword),
    path("AdminSetting",views.AdminSetting),
    path("CustomerSetting",views.CustomerSetting),
    path("book",views.book),
    path("CustomerPassword",views.CustomerPassword),
    path("CustomerContact",views.CustomerContact),
    path("CustomerEmail",views.CustomerEmail),
    path("CustomerCity",views.CustomerCity),
    path("Account",views.Account),
    path("AdminRegister",views.AdminRegister),
    path("Booking",views.Booking),
    path("EmployeeRegister",views.EmployeeRegister),
    path("CustomerRegister",views.CustomerRegister),
    path("Login",views.Login),
    path("AdminPasswordChange",views.AdminPasswordChange),
    path("AdminContactChange",views.AdminContactChange),
    path("AdminAddressChange",views.AdminAddressChange),
    path("AdminEmailChange",views.AdminEmailChange),
    path("EmpPasswordChange",views.EmpPasswordChange),
    path("EmpContactChange",views.EmpContactChange),
    path("EmpAddressChange",views.EmpAddressChange),
    path("EmpCityChange",views.EmpCityChange),
    path("CustomerPasswordChange",views.CustomerPasswordChange),
    path("CustomerContactChange",views.CustomerContactChange),
    path("CustomerCityChange",views.CustomerCityChange),
    path("CustomerEmailChange",views.CustomerEmailChange),
    path("ViewAllAccount",views.ViewAllAccount),
    path("AccountDelete",views.AccountDelete),
    path("EmployeeAccountDelete",views.EmployeeAccountDelete),
    path("SearchAccount",views.SearchAccount),
    path("SearchEmployee",views.SearchEmployee),
    path("GamingZone",views.GamingZone),
    path("GamingZoneRegister",views.GamingZoneRegister),
    path("AdminView", views.AdminView),
    path("ViewGamingZone", views.ViewGamingZone),
    path("ViewComplaint", views.ViewComplaint),
    path("ViewBooking", views.ViewBooking),
    path("CustomerView", views.CustomerView),
    path("Complaint", views.Complaint),
    path("ComplaintRegister", views.ComplaintRegister),
    path("EmployeeHome", views.EmployeeHome),
    path("EmployeeSetting", views.EmployeeSetting),
    path("EmployeeView", views.EmployeeView),
    path("ViewEmpGamingZone", views.ViewEmpGamingZone),
    path("ViewEmpComplaint", views.ViewEmpComplaint),
    path("ViewEmpBooking", views.ViewEmpBooking),
    path("EmpPassword", views.EmpPassword),
    path("EmpContact", views.EmpContact),
    path("EmpCity", views.EmpCity),
    path("EmpAddress", views.EmpAddress),
    path("EmpAccount", views.EmpAccount),
    path("EmpGamingZone", views.EmpGamingZone),
    path("EmpAccountDelete", views.EmpAccountDelete),
    path("EmpGamingZoneRegister", views.EmpGamingZoneRegister),
    path("EmpAccountDeletetion", views.EmpAccountDeletetion),
    path("logout", views.logout),
]
