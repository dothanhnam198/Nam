from django.contrib import admin
from .models import Student, Subject, Program
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'student_name', 'birth_day', 'grade', 'program']
    search_fields = ['student_id', 'student_name', 'grade']
admin.site.register(Student, StudentAdmin)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject_id', 'subject_name', 'TC']
    search_fields = ['subject_id', 'subject_name']
admin.site.register(Subject, SubjectAdmin)


class ProgramAdmin(admin.ModelAdmin):
    list_display = ['program_id', 'program_name']
    search_fields = ['program_id', 'program_name']

admin.site.register(Program, ProgramAdmin)