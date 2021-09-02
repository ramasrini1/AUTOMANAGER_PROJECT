"""automanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from management import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    
    #management
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('addcustomer/',  views.addcustomer, name='addcustomer'),
    path('customerlist/', views.customerlist, name='customerlist'),
    path('customers/', views.customers, name='customers'),
    path('customer/<int:customer_pk>', views.customer, name='customer'),
    path('customer/<int:customer_pk>/delete', views.deletecustomer, name='deletecustomer'),
    path('customer/<int:customer_pk>/edit', views.editcustomer, name='editcustomer'),
    

]
