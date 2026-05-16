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
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view

from .models import RoomAllocation

from .serializers import RoomAllocationSerializer

from rest_framework.response import Response

from rest_framework import status

from .serializers import StudentSerializer

from .serializers import StudentSerializer, RoomSerializer

from .serializers import ComplaintSerializer

from .models import Fee

from .serializers import FeeSerializer


from django.contrib.auth import authenticate, login, logout

from rest_framework.decorators import api_view

from rest_framework.response import Response

from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken




def student_signup(request):

    if request.method == "POST":

        username = request.POST.get("username")

        email = request.POST.get("email")

        password = request.POST.get("password")

        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:

            messages.error(
                request,
                "Passwords do not match"
            )

            return redirect("student-signup")

        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                "Username already exists"
            )

            return redirect("student-signup")

        user = User.objects.create_user(

            username=username,

            email=email,

            password=password
        )

        student = Student.objects.create(

            student_name=username,

            email=email,

            phone_number="0000000000",

            course="Not Assigned",

            year=1
        )

        StudentAccount.objects.create(

            user=user,

            student=student
        )

        messages.success(
            request,
            "Student account created successfully"
        )

        return redirect("student-login")

    return render(
        request,
        "accounts/student_signup.html"
    )
def student_dashboard(request):

    student_account = StudentAccount.objects.filter(
        user=request.user
    ).first()

    if not student_account:

        messages.error(
            request,
            "Student account not found"
        )

        return redirect("student-login")

    student = student_account.student

    total_rooms = Room.objects.count()

    available_beds = Room.objects.aggregate(
        total=models.Sum("available_beds")
    )["total"] or 0

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
        "dashboard/student_dashboard.html",
        context
    )


def student_login(request):

    if request.user.is_authenticated:

        return redirect("student-dashboard")

    if request.method == "POST":

        username = request.POST.get("username")

        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None and not user.is_staff:

            try:

                StudentAccount.objects.get(user=user)

                login(request, user)

                messages.success(
                    request,
                    "Student Login Successful"
                )

                return redirect("student-dashboard")

            except StudentAccount.DoesNotExist:

                messages.error(
                    request,
                    "Student account not found"
                )

        else:

            messages.error(
                request,
                "Invalid Username or Password"
            )

    return render(
        request,
        "accounts/student_login.html"
    )

def logout_view(request):

    is_admin = request.user.is_staff

    logout(request)

    if is_admin:

        messages.success(
            request,
            "Admin Logged Out Successfully"
        )

    else:

        messages.success(
            request,
            "Student Logged Out Successfully"
        )

    return redirect("homepage")

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

            messages.success(
                request,
                "Admin Login Successful"
            )

            return redirect("admin-dashboard")

        else:

            messages.error(
                request,
                "Admin access only"
            )

    return render(
    request,
    "accounts/admin_login.html"
)





def admin_dashboard(request):

    total_students = StudentAccount.objects.count()

    total_rooms = Room.objects.count()

    total_allocations = RoomAllocation.objects.count()

    available_beds = Room.objects.aggregate(
        total=models.Sum("available_beds")
    )["total"] or 0

    total_complaints = Complaint.objects.count()

    pending_complaints = Complaint.objects.filter(
        status="Pending"
    ).count()

    context = {

        "total_students": total_students,

        "total_rooms": total_rooms,

        "total_allocations": total_allocations,

        "available_beds": available_beds,

        "total_complaints": total_complaints,

        "pending_complaints": pending_complaints,

    }

    return render(
        request,
        "dashboard/admin_dashboard.html",
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

            messages.success(
                request,
                "Student Added Successfully"
            )

            return redirect("student-list")

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

    students_list = Student.objects.all()

    search = request.GET.get('search')

    course = request.GET.get('course')

    year = request.GET.get('year')

    if search:

        students_list = students_list.filter(
            student_name__icontains=search
        )

    if course:

        students_list = students_list.filter(
            course=course
        )

    if year:

        students_list = students_list.filter(
            year=year
        )

    paginator = Paginator(students_list, 5)

    page_number = request.GET.get('page')

    students = paginator.get_page(page_number)

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

        else:

            print(form.errors)

    else:

        form = RoomForm()

    return render(
        request,
        'rooms/add_room.html',
        {
            'form': form
        }
    )

def room_list(request):

    rooms = Room.objects.all()

    search = request.GET.get('search')

    room_type = request.GET.get('room_type')

    floor = request.GET.get('floor')

    if search:

        rooms = rooms.filter(
            room_number__icontains=search
        )

    if room_type:

        rooms = rooms.filter(
            room_type=room_type
        )

    if floor:

        rooms = rooms.filter(
            floor_number=floor
        )

    floors = Room.objects.values_list(
        'floor_number',
        flat=True
    ).distinct()

    context = {
        "rooms": rooms,
        "floors": floors
    }

    return render(
        request,
        "rooms/room_list.html",
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
        "allocations/allocate_room.html",
        context
    )



def allocation_list(request):

    allocation = RoomAllocation.objects.all()

    context = {
        "allocations": allocation
    }

    return render(
        request,
        "allocations/allocation_list.html",
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

    status = request.GET.get('status')

    if status:

        fees = fees.filter(status=status)

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

    complaints = Complaint.objects.all()

    status = request.GET.get('status')

    if status:

        complaints = complaints.filter(
            status=status
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

def withdraw_complaint(request, id):

    complaint = Complaint.objects.get(id=id)

    if complaint.status == "Pending":

        complaint.delete()

    return redirect("complaint-list")


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

def allocation_list(request):

    allocations = RoomAllocation.objects.all()

    student = request.GET.get("student")
    room = request.GET.get("room")
    date = request.GET.get("date")

    if student:

        allocations = allocations.filter(
            student__name__icontains=student
        )

    if room:

        allocations = allocations.filter(
            room__room_number__icontains=room
        )

    if date:

        allocations = allocations.filter(
            allocated_date=date
        )

    paginator = Paginator(allocations, 5)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj
    }

    return render(
        request,
        "allocations/allocation_list.html",
        context
    )

# ------------------------------------------------------------

#API's

# ------------------------------------------------------------

@api_view(["GET", "POST"])
def student_api(request):

    if request.method == "GET":

        students = Student.objects.all()

        serializer = StudentSerializer(
            students,
            many=True
        )

        return Response(serializer.data)

    elif request.method == "POST":

        serializer = StudentSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    

#Single Student API

@api_view(["GET", "PUT", "DELETE"])
def student_detail_api(request, id):

    try:

        student = Student.objects.get(id=id)

    except Student.DoesNotExist:

        return Response(
            {
                "error": "Student not found"
            },
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":

        serializer = StudentSerializer(student)

        return Response(serializer.data)

    elif request.method == "PUT":

        serializer = StudentSerializer(
            student,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":

        student.delete()

        return Response(
            {
                "message": "Student deleted successfully"
            },
            status=status.HTTP_200_OK
        )
    
# ------------------------------------------------------------
#Room API's
# ------------------------------------------------------------

@api_view(["GET", "POST"])
def room_api(request):

    if request.method == "GET":

        rooms = Room.objects.all()

        serializer = RoomSerializer(
            rooms,
            many=True
        )

        return Response(serializer.data)

    elif request.method == "POST":

        serializer = RoomSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
#single Room API

@api_view(["GET", "PUT", "DELETE"])
def room_detail_api(request, id):

    try:

        room = Room.objects.get(id=id)

    except Room.DoesNotExist:

        return Response(
            {
                "error": "Room not found"
            },
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":

        serializer = RoomSerializer(room)

        return Response(serializer.data)

    elif request.method == "PUT":

        serializer = RoomSerializer(room,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":

        room.delete()

        return Response(
            {
                "message": "Room deleted successfully"
            },
            status=status.HTTP_200_OK
        )

@api_view(["GET", "POST"])
def complaint_api(request):

    if request.method == "GET":

        complaints = Complaint.objects.all()

        status_filter = request.GET.get("status")

        if status_filter:

            complaints = complaints.filter(
                status=status_filter
            )

        serializer = ComplaintSerializer(
            complaints,
            many=True
        )

        return Response(serializer.data)

    elif request.method == "POST":

        serializer = ComplaintSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

#single Complaint API

@api_view(["GET", "PUT", "DELETE"])
def complaint_detail_api(request, id):

    try:

        complaint = Complaint.objects.get(id=id)

    except Complaint.DoesNotExist:

        return Response(
            {
                "error": "Complaint not found"
            },
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":

        serializer = ComplaintSerializer(complaint)

        return Response(serializer.data)

    elif request.method == "PUT":

        serializer = ComplaintSerializer(
            complaint,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":

        complaint.delete()

        return Response(
            {
                "message": "Complaint deleted successfully"
            },
            status=status.HTTP_200_OK
        )
    
#withdraw complaint API

@api_view(["PUT"])
def withdraw_complaint_api(request, id):

    try:

        complaint = Complaint.objects.get(id=id)

    except Complaint.DoesNotExist:

        return Response(
            {
                "error": "Complaint not found"
            },
            status=status.HTTP_404_NOT_FOUND
        )

    complaint.status = "Withdrawn"

    complaint.save()

    return Response(
        {
            "message": "Complaint withdrawn successfully"
        },
        status=status.HTTP_200_OK
    )

@api_view(["GET", "POST"])
def allocation_api(request):

    if request.method == "GET":

        allocations = RoomAllocation.objects.all()

        serializer = RoomAllocationSerializer(
            allocations,
            many=True
        )

        return Response(serializer.data)

    elif request.method == "POST":

        serializer = RoomAllocationSerializer(
            data=request.data
        )

        if serializer.is_valid():

            room = serializer.validated_data["room"]

            if room.available_beds <= 0:

                return Response(
                    {
                        "error": "No beds available"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            serializer.save()

            room.available_beds -= 1

            room.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
#single Allocation API

@api_view(["GET", "PUT", "DELETE"])
def allocation_detail_api(request, id):

    try:

        allocation = RoomAllocation.objects.get(id=id)

    except RoomAllocation.DoesNotExist:

        return Response(
            {
                "error": "Allocation not found"
            },
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":

        serializer = RoomAllocationSerializer(allocation)

        return Response(serializer.data)

    elif request.method == "PUT":

        serializer = RoomAllocationSerializer(
            allocation,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":

        room = allocation.room

        room.available_beds += 1

        room.save()

        allocation.delete()

        return Response(
            {
                "message": "Allocation deleted successfully"
            },
            status=status.HTTP_200_OK
        )
    
@api_view(["GET", "POST"])
def fee_api(request):

    if request.method == "GET":

        fees = Fee.objects.all()

        status_filter = request.GET.get("status")

        if status_filter:

            fees = fees.filter(
                payment_status=status_filter
            )

        serializer = FeeSerializer(
            fees,
            many=True
        )

        return Response(serializer.data)

    elif request.method == "POST":

        serializer = FeeSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

#single Fee API

@api_view(["GET", "PUT", "DELETE"])
def fee_detail_api(request, id):

    try:

        fee = Fee.objects.get(id=id)

    except Fee.DoesNotExist:

        return Response(
            {
                "error": "Fee record not found"
            },
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":

        serializer = FeeSerializer(fee)

        return Response(serializer.data)

    elif request.method == "PUT":

        serializer = FeeSerializer(
            fee,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":

        fee.delete()

        return Response(
            {
                "message": "Fee deleted successfully"
            },
            status=status.HTTP_200_OK
        )
    
def get_tokens_for_user(user):

    refresh = RefreshToken.for_user(user)

    return {

        'refresh': str(refresh),

        'access': str(refresh.access_token),

    }

@api_view(["POST"])
def student_login_api(request):

    username = request.data.get("username")

    password = request.data.get("password")

    user = authenticate(
        username=username,
        password=password
    )

    if user is not None:

        tokens = get_tokens_for_user(user)

        return Response(
            {
                "message": "Student login successful",
                "username": user.username,
                "tokens": tokens
            },
            status=status.HTTP_200_OK
        )

    return Response(
        {
            "error": "Invalid username or password"
        },
        status=status.HTTP_401_UNAUTHORIZED
    )

@api_view(["POST"])
def admin_login_api(request):

    username = request.data.get("username")

    password = request.data.get("password")

    user = authenticate(
        username=username,
        password=password
    )

    if user is not None and user.is_staff:

        tokens = get_tokens_for_user(user)

        return Response(
            {
                "message": "Admin login successful",
                "username": user.username,
                "tokens": tokens
            },
            status=status.HTTP_200_OK
        )

    return Response(
        {
            "error": "Invalid admin credentials"
        },
        status=status.HTTP_401_UNAUTHORIZED
    )