from django.urls import path

from . import views


urlpatterns = [

    path(
        "students/",
        views.student_api,
        name="student-api"
    ),

    path(
        "students/<int:id>/",
        views.student_detail_api,
        name="student-detail-api"
    ),


    path(
    "rooms/",
    views.room_api,
    name="room-api"
),

path(
    "rooms/<int:id>/",
    views.room_detail_api,
    name="room-detail-api"
),

]