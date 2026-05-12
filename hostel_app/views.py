from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student
from django.shortcuts import get_object_or_404
from .models import Student, Room
from .forms import StudentForm, RoomForm
from .forms import RoomAllocationForm
from .models import RoomAllocation
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import models
from .models import Fee
from .forms import FeeForm
from .models import Complaint
from .forms import ComplaintForm
from django.http import JsonResponse
from django.contrib.auth.models import User
from .forms import StudentSignupForm
from .models import Student
from .models import StudentAccount


from django.contrib.auth import (
    authenticate,
    login,
    logout
)


def student_signup(request):

    form = StudentSignupForm()

    if request.method == "POST":

        form = StudentSignupForm(request.POST)

        if form.is_valid():

            user = form.save()

            student = Student.objects.create(

                student_name=user.username,

                email=form.cleaned_data["email"],

                phone_number="0000000000",

                course="Not Assigned",

                year=1
            )

            StudentAccount.objects.create(

                user=user,

                student=student
            )

            login(request, user)

            return redirect("student-dashboard")

        else:

            print(form.errors)

        

    context = {

        "form": form
    }

    return render(
        request,
        "student_signup.html",
        context
    )


def student_dashboard(request):

    student_account = StudentAccount.objects.get(
        user=request.user
    )

    student = student_account.student

    total_rooms = Room.objects.count()

    available_beds = Room.objects.aggregate(
        total=models.Sum("available_beds")
    )["total"]

    my_complaints = Complaint.objects.filter(
        student=student
    ).count()

    pending_complaints = Complaint.objects.filter(
        student=student,
        status="Pending"
    ).count()

    allocation = RoomAllocation.objects.filter(
        student=student
    ).first()

    context = {

        "total_rooms": total_rooms,

        "available_beds": available_beds,

        "my_complaints": my_complaints,

        "pending_complaints": pending_complaints,

        "allocation": allocation

    }

    return render(
        request,
        "student_dashboard.html",
        context
    )


def student_login(request):

    if request.method == "POST":

        username = request.POST.get("username")

        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None and not user.is_staff:

            login(request, user)

            return redirect("homepage")

        else:

            messages.error(
                request,
                "Student access only"
            )

    return render(
        request,
        "student_login.html"
    )

def admin_login(request):

    if request.method == "POST":

        username = request.POST.get("username")

        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None and user.is_staff:

            login(request, user)

            return redirect("admin-dashboard")

        else:

            messages.error(
                request,
                "Admin access only"
            )

    return render(
        request,
        "admin_login.html"
    )
def admin_dashboard(request):

    total_students = Student.objects.count()

    total_rooms = Room.objects.count()

    total_allocations = RoomAllocation.objects.count()

    total_complaints = Complaint.objects.count()

    pending_complaints = Complaint.objects.filter(
        status="Pending"
    ).count()

    available_beds = Room.objects.aggregate(
        total=models.Sum("available_beds")
    )["total"]

    context = {

        "total_students": total_students,

        "total_rooms": total_rooms,

        "total_allocations": total_allocations,

        "total_complaints": total_complaints,

        "pending_complaints": pending_complaints,

        "available_beds": available_beds

    }

    return render(
        request,
        "admin_dashboard.html",
        context
    )

def homepage(request):

    total_students = Student.objects.count()

    total_rooms = Room.objects.count()

    total_allocations = RoomAllocation.objects.count()

    available_beds = Room.objects.aggregate(
        total=models.Sum('available_beds')
    )['total']

    context = {

        "total_students": total_students,

        "total_rooms": total_rooms,

        "total_allocations": total_allocations,

        "available_beds": available_beds
    }

    return render(
        request,
        "homepage.html",
        context
    )


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
        "students": students
    }

    return render(
        request,
        "students/student_list.html",
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


def delete_student(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    student.delete()

    return redirect('student-list')


def student_details(request, id):

    student = Student.objects.get(id=id)

    context = {
        "student": student
    }

    return render(
        request,
        "students/student_details.html",
        context
    )


def add_room(request):

    if request.method == "POST":

        form = RoomForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('room-list') 

    form = RoomForm()

    context = {
        'form': form
    }

    return render(
        request,
        'rooms/add_room.html',
        context
    )


def room_list(request):

    rooms = Room.objects.all()

    context = {
        'rooms': rooms
    }

    return render(
        request,
        'rooms/room_list.html',
        context
    )


def room_details(request, id):

    room = get_object_or_404(
        Room,
        id=id
    )

    context = {
        'room': room
    }

    return render(
        request,
        'rooms/room_details.html',
        context
    )


def update_room(request, id):

    room = get_object_or_404(Room, id=id)

    form = RoomForm(instance=room)

    if request.method == "POST":

        form = RoomForm(request.POST, instance=room)

        if form.is_valid():

            form.save()

            return redirect("room-list")

    context = {
        "form": form
    }

    return render(
        request,
        "rooms/update_room.html",
        context
    )


def delete_room(request, id):

    room = get_object_or_404(Room, id=id)

    room.delete()

    return redirect("room-list")


def allocate_room(request):

    available_rooms = Room.objects.filter(
        available_beds__gt=0
    )

    form = RoomAllocationForm()

    form.fields["room"].queryset = available_rooms

    if request.method == "POST":

        form = RoomAllocationForm(request.POST)

        form.fields["room"].queryset = available_rooms

        if form.is_valid():

            student = form.cleaned_data["student"]

            already_allocated = RoomAllocation.objects.filter(
                student=student
            ).exists()

            if already_allocated:

                messages.error(
                    request,
                    "Student already has a room allocated."
                )

                return redirect("allocate-room")

            allocation = form.save()

            room = allocation.room

            room.available_beds -= 1

            room.save()

            messages.success(
                request,
                "Room allocated successfully."
            )

            return redirect("allocation-list")

    context = {
        "form": form
    }

    return render(
        request,
        "allocation/allocate_room.html",
        context
    )



def allocation_list(request):

    allocations = RoomAllocation.objects.all()

    context = {
        "allocations": allocations
    }

    return render(
        request,
        "allocation/allocation_list.html",
        context
    )

def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")

        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("homepage")

        else:

            messages.error(
                request,
                "Invalid username or password"
            )

    return render(
        request,
        "login.html"
    )
def logout_view(request):

    logout(request)

    return redirect("homepage")


def add_fee(request):

    form = FeeForm()

    if request.method == "POST":

        form = FeeForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("fee-list")

    context = {
        "form": form
    }

    return render(
        request,
        "fees/add_fee.html",
        context
    )



def fee_list(request):

    fees = Fee.objects.all()

    context = {
        "fees": fees
    }

    return render(
        request,
        "fees/fee_list.html",
        context
    )



def update_fee(request, id):

    fee = Fee.objects.get(id=id)

    form = FeeForm(instance=fee)

    if request.method == "POST":

        form = FeeForm(
            request.POST,
            instance=fee
        )

        if form.is_valid():

            form.save()

            return redirect("fee-list")

    context = {
        "form": form
    }

    return render(
        request,
        "fees/update_fee.html",
        context
    )



def delete_fee(request, id):

    fee = Fee.objects.get(id=id)

    fee.delete()

    return redirect("fee-list")





def add_complaint(request):

    if request.method == "POST":

        student_account = StudentAccount.objects.get(
            user=request.user
        )

        Complaint.objects.create(

            student=student_account.student,

            title=request.POST.get("title"),

            description=request.POST.get("description"),

            status="Pending"

        )

        return redirect("complaint-list")

    return render(
        request,
        "complaints/add_complaint.html"
    )



def complaint_list(request):

    if request.user.is_staff:

        complaints = Complaint.objects.all()

    else:

        student_account = StudentAccount.objects.get(
            user=request.user
        )

        complaints = Complaint.objects.filter(
            student=student_account.student
        )

    context = {
        "complaints": complaints
    }

    return render(
        request,
        "complaints/complaint_list.html",
        context
    )


def complaint_details(request, id):

    complaint = Complaint.objects.get(id=id)

    context = {
        "complaint": complaint
    }

    return render(
        request,
        "complaints/complaint_details.html",
        context
    )




def update_complaint(request, id):

    complaint = Complaint.objects.get(id=id)

    if request.method == "POST":

        form = ComplaintForm(request.POST)

        if form.is_valid():

            student_id = form.cleaned_data["student_id"]

            student = Student.objects.get(
                id=student_id
            )

            complaint.student = student

            complaint.title = form.cleaned_data["title"]

            complaint.description = form.cleaned_data["description"]

            complaint.status = form.cleaned_data["status"]

            complaint.save()

            return redirect("complaint-list")

    else:

        form = ComplaintForm(
            initial={
                "student_id": complaint.student.id,
                "title": complaint.title,
                "description": complaint.description,
                "status": complaint.status
            }
        )

    context = {
        "form": form
    }

    return render(
        request,
        "complaints/update_complaint.html",
        context
    )


def delete_complaint(request, id):

    complaint = Complaint.objects.get(id=id)

    complaint.delete()

    return redirect("complaint-list")


def get_student(request):

    student_id = request.GET.get("student_id")

    try:

        student = Student.objects.get(id=student_id)

        data = {
            "name": student.student_name
        }

    except Student.DoesNotExist:

        data = {
            "name": "Student Not Found"
        }

    return JsonResponse(data)

def allocation_details(request, id):

    allocation = RoomAllocation.objects.get(id=id)

    context = {
        "allocation": allocation
    }

    return render(
        request,
        "allocations/allocation_details.html",
        context
    )

def update_allocation(request, id):

    allocation = RoomAllocation.objects.get(id=id)

    form = RoomAllocationForm(instance=allocation)

    if request.method == "POST":

        form = RoomAllocationForm(
            request.POST,
            instance=allocation
        )

        if form.is_valid():

            form.save()

            return redirect("allocation-list")

    context = {
        "form": form
    }

    return render(
        request,
        "allocations/update_allocation.html",
        context
    )


def delete_allocation(request, id):

    allocation = RoomAllocation.objects.get(id=id)

    allocation.delete()

    return redirect("allocation-list")