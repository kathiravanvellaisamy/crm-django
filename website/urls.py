from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home,name='home'),
    path('login/', views.login_user,name='login'),
    path('logout/', views.logout_user,name='logout'),
    path('register/', views.register,name='register'),
    path('dashboard/', views.dashboard,name='dashboard'),
    path('customer/<int:pk>', views.customer_profile,name='customer'),
    path('delete_customer/<int:pk>', views.delete_customer,name='delete_customer'),
    path('add_customer/', views.add_customer,name='add_customer'),
    path('update_customer/<int:pk>', views.update_customer,name='update_customer'),
]
