from django.db import models

# Create your models here.



class Program(models.Model):
    program_id = models.CharField(max_length=50, primary_key=True)
    program_name = models.CharField(max_length=50)

    def __str__(self):
        return self.program_name


class Subject(models.Model):
    subject_id = models.CharField(max_length=20,primary_key=True)
    subject_name = models.CharField(max_length=50)
    TC = models.IntegerField()
    program = models.ManyToManyField(Program, blank=True, null=True)

    def __str__(self):
        return self.subject_name


class Student(models.Model):
    student_id = models.CharField(max_length=50, primary_key=True)
    student_name = models.CharField(max_length=50)
    birth_day = models.DateField(blank=True, null=True)
    grade = models.CharField(max_length=20)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, blank=True, null=True)
    subject = models.ManyToManyField(Subject, blank= True, null=True)

    def __str__(self):
        return self.student_name