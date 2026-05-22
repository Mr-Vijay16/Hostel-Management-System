Hostel Management System

A full-stack Django-based Hostel Management System designed to manage students, rooms, room allocations, fees, and complaints efficiently. The project also includes REST APIs, JWT Authentication, and online deployment using Render.

Live Project

Hostel Management System Live Demo

Features
Authentication
Admin Login
Student Login
Student Signup
JWT Authentication for APIs
Student Management
Add Student
Update Student
Delete Student
View Student Details
Search & Filter Students
Pagination
Room Management
Add Rooms
Update Rooms
Delete Rooms
Track Available Beds
Room Type Management (AC / Non-AC)
Room Allocation
Allocate Rooms to Students
Prevent Duplicate Allocations
Automatically Reduce Available Beds
Allocation Details View
Fee Management
Add Fee Records
Update Payment Status
Pending / Paid Tracking
Filter Fees
Complaint Management
Students Can Raise Complaints
Complaint Status Tracking
Pending / Resolved Complaints
Complaint Filtering
REST APIs
Student APIs
Room APIs
Fee APIs
Complaint APIs
Allocation APIs
Admin Login API
Technologies Used
Frontend
HTML
CSS
Bootstrap
Backend
Django
Django REST Framework
Database
SQLite
Authentication
JWT Authentication
Deployment
Render
Project Structure
hostel_management/
│
├── hostel_management/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── hostel_app/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── serializers.py
│   ├── urls.py
│
├── templates/
├── static/
├── manage.py
├── requirements.txt
├── Procfile
Database Relationships
One User ↔ One StudentAccount
One Student → Many Complaints
One Student → Many Fees
One Room → Many Allocations
API Endpoints
Students
GET     /api/students/
POST    /api/students/
GET     /api/students/<id>/
PUT     /api/students/<id>/
DELETE  /api/students/<id>/
Rooms
GET     /api/rooms/
POST    /api/rooms/
GET     /api/rooms/<id>/
PUT     /api/rooms/<id>/
DELETE  /api/rooms/<id>/
Fees
GET     /api/fees/
POST    /api/fees/
GET     /api/fees/<id>/
PUT     /api/fees/<id>/
DELETE  /api/fees/<id>/
Complaints
GET     /api/complaints/
POST    /api/complaints/
GET     /api/complaints/<id>/
PUT     /api/complaints/<id>/
DELETE  /api/complaints/<id>/
Allocations
GET     /api/allocations/
POST    /api/allocations/
GET     /api/allocations/<id>/
PUT     /api/allocations/<id>/
DELETE  /api/allocations/<id>/
JWT Authentication API
Admin Login API
POST /api/admin-login/
Request Body
{
    "username": "vijay",
    "password": "1612"
}
Response
{
    "message": "Admin login successful",
    "tokens": {
        "refresh": "refresh_token",
        "access": "access_token"
    }
}
Installation
Clone Repository
git clone https://github.com/YOUR_USERNAME/hostel-management-system.git
Create Virtual Environment
python -m venv env
Activate Environment
Windows
env\Scripts\activate
Linux/Mac
source env/bin/activate
Install Requirements
pip install -r requirements.txt
Run Migrations
python manage.py makemigrations
python manage.py migrate
Create Superuser
python manage.py createsuperuser
Run Server
python manage.py runserver
Deployment

The project is deployed on Render using:

Gunicorn
WhiteNoise
SQLite Database
Future Enhancements
Hostel Attendance System
Student Profile Photos
Role-Based Access Control
Authors
H S Vijay,
C Jyothika,
G Jeevana Lalitha

#Full Stack Django Developer
#python Developer
