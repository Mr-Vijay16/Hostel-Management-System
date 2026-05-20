from django.urls import path

from . import views


urlpatterns = [

    path(
        "students/",
        views.student_api,
        name="student-api"
    ),

  

    path(
    "rooms/",
    views.room_api,
    name="room-api"
),

path(
    'rooms/<int:pk>/',
    views.room_detail_api,
    name='room-detail'
),


path(
    "complaints/",
    views.complaint_api,
    name="complaint-api"
),

path(
    'complaints/<int:pk>/',
    views.complaint_detail_api,
    name='complaint-detail'
),

path(
    'withdraw-complaint/<int:id>/',
    views.withdraw_complaint,
    name='withdraw-complaint'
),

path(
    "allocations/",
    views.allocation_api,
    name="allocation-api"
),

path(
    'allocations/<int:pk>/',
    views.allocation_detail_api,
    name='allocation-detail'
),

path(
    "fees/",
    views.fee_api,
    name="fee-api"
),

path(
    'fees/<int:pk>/',
    views.fee_detail_api,
    name='fee-detail'
),

path(
    "student-login/",
    views.student_login_api,
    name="student-login-api"
),

path(
    "admin-login/",
    views.admin_login_api,
    name="admin-login-api"
),


path(
    "admin-dashboard/",
    views.admin_dashboard_api,
    name="admin-dashboard-api"
),

path(
    'student-dashboard/',
    views.student_dashboard,
    name='student-dashboard'
),

path(
    'students/<int:pk>/',
    views.student_detail_api,
    name='student-detail'
),
]