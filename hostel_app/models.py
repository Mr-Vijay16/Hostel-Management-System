from django.db import models
from django.contrib.auth.models import User


class StudentAccount(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    student = models.OneToOneField(
        "Student",
        on_delete=models.CASCADE
    )

    def __str__(self):

        return self.user.username
class Student(models.Model):

    student_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone_number = models.CharField(max_length=15)

    course = models.CharField(max_length=100)

    year = models.IntegerField()

    def __str__(self):

        return f"{self.id} - {self.student_name}"


class Room(models.Model):

    room_number = models.CharField(
        max_length=20,
        unique=True
    )

    room_type = models.CharField(
        max_length=50
    )

    total_beds = models.IntegerField()

    available_beds = models.IntegerField()

    floor_number = models.IntegerField()

    def __str__(self):

        return self.room_number


class RoomAllocation(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE
    )

    allocation_date = models.DateField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.student} - {self.room}"


class Fee(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    amount = models.IntegerField()

    payment_date = models.DateField()

    status = models.CharField(
        max_length=20
    )

    def __str__(self):

        return self.student.student_name


class Complaint(models.Model):

    STATUS_CHOICES = [

        ("Pending", "Pending"),

        ("In Progress", "In Progress"),

        ("Resolved", "Resolved")
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    complaint_date = models.DateField(
        auto_now_add=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )

    def __str__(self):

        return self.title

    

    def __str__(self):

        return self.title