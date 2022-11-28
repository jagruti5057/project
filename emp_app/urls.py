from django.urls import path
from emp_app import views

urlpatterns = [
     path('', views.index, name='index'),
     path('all_emp', views.all_emp, name='all_emp'),
     path('add_emp', views.add_emp, name='add_emp'),
     path('edit_emp/<int:emp_id>', views.edit_emp, name='edit_emp'),
     # path('edit_employee', views.edit_emp, name='edit_emp'),
     path('delete_emp/<int:emp_id>', views.delete_emp, name='delete_emp'),
     
     # path('delete_emp', views.delete_emp, name='delete_emp'),

]