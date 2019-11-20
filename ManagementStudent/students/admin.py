from django.contrib import admin
from .models import Student, Subject, Program, Results, Courses, CourseRegistration, Semester
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


class CoursesAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'subject', 'period', 'day', 'room']
    search_fields = ['course_id', 'subject__subject_name']
admin.site.register(Courses, CoursesAdmin)


class CourseRegistrationAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'semester', 'date_opened', 'date_closed']
    search_fields = ['student__student_name', 'course__course_id', 'semester__semester_id']
admin.site.register(CourseRegistration, CourseRegistrationAdmin)


class ResultsAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'semester', 'score_middle', 'score_final']
    search_fields = ['student__student_name', 'subject__subject_name', 'semester__semester_id']
admin.site.register(Results, ResultsAdmin)


class SemesterAdmin(admin.ModelAdmin):
    list_display = ['semester_id']
    search_fields = ['semester_id']
admin.site.register(Semester, SemesterAdmin)
