from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('add-student/',views.add_student,name='add-student'),
    path('student-list/',views.student_list, name='student-list'),
    path('update-student/<int:id>/',views.update_student,name='update-student'),
]