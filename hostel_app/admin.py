from django.contrib import admin
from .models import Student
from .models import Room
from .models import Fee
from .models import Complaint

# Register your models here.
admin.site.register(Student)
admin.site.register(Room)
admin.site.register(Fee)
admin.site.register(Complaint)