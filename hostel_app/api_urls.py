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


path(
    "complaints/",
    views.complaint_api,
    name="complaint-api"
),

path(
    "complaints/<int:id>/",
    views.complaint_detail_api,
    name="complaint-detail-api"
),

path(
    "complaints/withdraw/<int:id>/",
    views.withdraw_complaint_api,
    name="withdraw-complaint-api"
),

path(
    "allocations/",
    views.allocation_api,
    name="allocation-api"
),

path(
    "allocations/<int:id>/",
    views.allocation_detail_api,
    name="allocation-detail-api"
),

path(
    "fees/",
    views.fee_api,
    name="fee-api"
),

path(
    "fees/<int:id>/",
    views.fee_detail_api,
    name="fee-detail-api"
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
    "student-dashboard/<int:student_id>/",
    views.student_dashboard_api,
    name="student-dashboard-api"
),

]