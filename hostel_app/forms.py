from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:

        model = Student

        fields = [
            "student_name",
            "email",
            "phone_number",
            "course",
            "year",
        ]