from django.forms import ModelForm
from .models import Student

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'student_name', 'birth_day', 'grade', 'program']
