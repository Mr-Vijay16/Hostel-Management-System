from django.urls import path
from . import views



urlpatterns = [
    path('', views.homepage, name='homepage'),

    path(
    "student-signup/",
    views.student_signup,
    name="student-signup"
),

path(
    "student-login/",
    views.student_login,
    name="student-login"
),

path(
    "admin-login/",
    views.admin_login,
    name="admin-login"
),

    path('add-student/',views.add_student,name='add-student'),
    path('student-list/',views.student_list, name='student-list'),
    path('update-student/<int:id>/',views.update_student,name='update-student'),
    path('delete-student/<int:id>/',views.delete_student,name='delete-student'),
    path('student-details/<int:id>/',views.student_details,name='student-details'),
    path('add-room/',views.add_room,name='add-room'),
    path('room-list/',views.room_list,name='room-list'),
    path('room-details/<int:id>/',views.room_details, name='room-details'),
    path("update-room/<int:id>/",views.update_room,name="update-room"),
    path("delete-room/<int:id>/",views.delete_room,name="delete-room"),
    path("allocate-room/",views.allocate_room,name="allocate-room"),
    path("logout/",views.logout_view,name="logout"),
    path(
    "add-fee/",
    views.add_fee,
    name="add-fee"
),

path(
    "fee-list/",
    views.fee_list,
    name="fee-list"
),

path(
    "update-fee/<int:id>/",
    views.update_fee,
    name="update-fee"
),

path(
    "delete-fee/<int:id>/",
    views.delete_fee,
    name="delete-fee"
),

path(
    "add-complaint/",
    views.add_complaint,
    name="add-complaint"
),

path(
    "complaint-list/",
    views.complaint_list,
    name="complaint-list"
),

path(
    "complaint-details/<int:id>/",
    views.complaint_details,
    name="complaint-details"
),

path(
    "update-complaint/<int:id>/",
    views.update_complaint,
    name="update-complaint"
),

path(
    "withdraw-complaint/<int:id>/",
    views.withdraw_complaint,
    name="withdraw-complaint"
),

path(
    "delete-complaint/<int:id>/",
    views.delete_complaint,
    name="delete-complaint"
),
path(
    "get-student/",
    views.get_student,
    name="get-student"
),
path(
    "allocation-details/<int:id>/",
    views.allocation_details,
    name="allocation-details"
),

path(
    "update-allocation/<int:id>/",
    views.update_allocation,
    name="update-allocation"
),

path(
    "delete-allocation/<int:id>/",
    views.delete_allocation,
    name="delete-allocation"
),
path(
    "allocation-list/",
    views.allocation_list,
    name="allocation-list"
),
path(
    "student-dashboard/",
    views.student_dashboard,
    name="student-dashboard"
),
path(
    "admin-dashboard/",
    views.admin_dashboard,
    name="admin-dashboard"
),


]