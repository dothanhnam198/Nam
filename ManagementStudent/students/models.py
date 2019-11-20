from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Program(models.Model):
    program_id = models.CharField(max_length=50, primary_key=True)
    program_name = models.CharField(max_length=50)

    def __str__(self):
        return self.program_name


class Semester(models.Model):
    semester_id = models.IntegerField(primary_key=True)

    def __int__(self):
        return self.semester_id


class Subject(models.Model):
    subject_id = models.CharField(max_length=20,primary_key=True)
    subject_name = models.CharField(max_length=50)
    TC = models.IntegerField()
    program = models.ManyToManyField(Program, blank=True, null=True)

    def __str__(self):
        return self.subject_name


class Courses(models.Model):
    course_id = models.CharField(max_length=20, primary_key=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    period = models.CharField(max_length=20)
    day = models.CharField(max_length=20)
    room = models.CharField(max_length=20)

    def __str__(self):
        return self.course_id


class Student(models.Model):
    student_id = models.CharField(max_length=50, primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,default=student_id, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=50)
    birth_day = models.DateField(blank=True, null=True)
    grade = models.CharField(max_length=20)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.student_name


class CourseRegistration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    date_opened = models.DateField()
    date_closed = models.DateField()


class Results(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    score_middle = models.FloatField()
    score_final = models.FloatField()


