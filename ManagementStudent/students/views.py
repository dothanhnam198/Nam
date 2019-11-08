from django.shortcuts import render
from .models import Student, Subject, Program
from .form import StudentForm
from django.http import JsonResponse
# Create your views here.


def index(request):
    return render(request, 'students.html')


def course(request):
    return render(request, 'course.html')


def student_program(request):
    return render(request, 'studentprogram.html')


def student_list(request):
    obj = Student.objects.all()

    context = {'students': obj}

    return render(request, 'student_list.html', context)



def course(request):
    obj = Subject.objects.all()

    context = {'subjects': obj}

    return render(request, 'course.html', context)


def program(request):
    obj = Program.objects.all()

    context = {'programs': obj}

    return render(request, 'program.html', context)


def program_details(request, id):
    obj = Program.subject.get(id=id)


def add_student(request):
        form = StudentForm(request.POST)
        return render(request, 'student_form.html', {'form': form})