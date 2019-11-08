from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('student_list/', views.student_list),
    path('course/', views.course),
    path('program/', views.program),
    path('program/<int:id>', views.program_details),
    path('studentprogram/', views.student_program),
    path('add/student/', views.add_student)
]