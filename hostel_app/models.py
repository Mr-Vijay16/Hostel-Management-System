from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):

    student_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone_number = models.CharField(max_length=15)

    course = models.CharField(max_length=100)

    year = models.IntegerField()

    def __str__(self):

        return self.student_name
