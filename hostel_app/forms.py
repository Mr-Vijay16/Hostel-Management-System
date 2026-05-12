from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from .models import (
    Student,
    Room,
    RoomAllocation,
    Fee
)

class StudentSignupForm(UserCreationForm):

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:

        model = User

        fields = [
            "username",
            "email",
            "password1",
            "password2"
        ]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            "class": "form-control"
        })

        self.fields["password1"].widget.attrs.update({
            "class": "form-control"
        })

        self.fields["password2"].widget.attrs.update({
            "class": "form-control"
        })

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


class RoomForm(forms.ModelForm):

    class Meta:

        model = Room

        fields = [
            "room_number",
            "room_type",
            "total_beds",
            "available_beds",
            "floor_number",
        ]


class RoomAllocationForm(forms.ModelForm):

    class Meta:

        model = RoomAllocation

        fields = [
            "student",
            "room"
        ]


class FeeForm(forms.ModelForm):

    class Meta:

        model = Fee

        fields = "__all__"

        widgets = {

            "payment_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            )
        }


class ComplaintForm(forms.Form):

    STATUS_CHOICES = [

        ("Pending", "Pending"),

        ("In Progress", "In Progress"),

        ("Resolved", "Resolved")
    ]

    student_id = forms.IntegerField()

    title = forms.CharField(
        max_length=200
    )

    description = forms.CharField(
        widget=forms.Textarea
    )

    status = forms.ChoiceField(
        choices=STATUS_CHOICES
    )