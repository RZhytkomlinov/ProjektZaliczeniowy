from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('hour_table/<str:pk>/', views.hour_table, name="hour_table"),
    path('home_employee/', views.home_employee, name='home_employee'),
    path('update_employee/<str:pk>/', views.update_employee, name='update_employee'),
    path('delete_employee/<str:pk>/', views.delete_employee, name='delete_employee'),

]

"""
customer - hourtable
userpage - home_emp
"""