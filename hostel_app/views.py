from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student
from django.shortcuts import get_object_or_404

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def add_student(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('student-list')

    form = StudentForm()

    context = {
        'form': form
    }

    return render(
        request,
        'students/add_student.html',
        context
    )

def student_list(request):

    students = Student.objects.all()

    context = {
        'students': students
    }

    return render(
        request,
        'students/student_list.html',
        context
    )

def update_student(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    if request.method == "POST":

        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():

            form.save()

            return redirect('student-list')

    form = StudentForm(instance=student)

    context = {
        'form': form
    }

    return render(
        request,
        'students/update_student.html',
        context
    )