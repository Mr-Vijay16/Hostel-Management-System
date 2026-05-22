# 🏨 Hostel Management System

A full-stack Django-based Hostel Management System designed to manage students, rooms, room allocations, fees, and complaints efficiently.

🚀 The project also includes:
- REST APIs
- JWT Authentication
- Admin & Student Dashboards
- Online Deployment using Render

---

# 🌐 Live Demo

🔗 https://hostel-management-system-aawv.onrender.com/

---

# 📌 Features

## 🔐 Authentication
- Admin Login
- Student Login
- Student Signup
- JWT Authentication for APIs

---

## 👨‍🎓 Student Management
- Add Student
- Update Student
- Delete Student
- Search Students
- Pagination

---

## 🏠 Room Management
- Add Rooms
- Update Rooms
- Delete Rooms
- Track Available Beds
- AC / Non-AC Rooms

---

## 🛏️ Room Allocation
- Allocate Rooms
- Prevent Duplicate Allocations
- Auto Reduce Available Beds

---

## 💰 Fee Management
- Add Fee Records
- Payment Status Tracking
- Pending / Paid Fees

---

## 📝 Complaint Management
- Raise Complaints
- Complaint Status Tracking
- Pending / Resolved Complaints

---

# 🛠️ Technologies Used

| Frontend | Backend | Database | Deployment |
|---|---|---|---|
| HTML | Django | SQLite | Render |
| CSS | Django REST Framework |  | Gunicorn |
| Bootstrap | JWT Authentication |  | WhiteNoise |

---

# 📂 Project Structure

```bash
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
```

---

# 🔗 Database Relationships

- One User ↔ One StudentAccount
- One Student → Many Complaints
- One Student → Many Fees
- One Room → Many Allocations

---

# 🚀 API Endpoints

## 👨‍🎓 Student APIs

```http
GET     /api/students/
POST    /api/students/
GET     /api/students/<id>/
PUT     /api/students/<id>/
DELETE  /api/students/<id>/
```

---

## 🏠 Room APIs

```http
GET     /api/rooms/
POST    /api/rooms/
GET     /api/rooms/<id>/
PUT     /api/rooms/<id>/
DELETE  /api/rooms/<id>/
```

---

## 💰 Fee APIs

```http
GET     /api/fees/
POST    /api/fees/
GET     /api/fees/<id>/
PUT     /api/fees/<id>/
DELETE  /api/fees/<id>/
```

---

## 📝 Complaint APIs

```http
GET     /api/complaints/
POST    /api/complaints/
GET     /api/complaints/<id>/
PUT     /api/complaints/<id>/
DELETE  /api/complaints/<id>/
```

---

## 🛏️ Allocation APIs

```http
GET     /api/allocations/
POST    /api/allocations/
GET     /api/allocations/<id>/
PUT     /api/allocations/<id>/
DELETE  /api/allocations/<id>/
```

---

# 🔑 JWT Authentication API

## Admin Login API

```http
POST /api/admin-login/
```

### Request Body

```json
{
    "username": "vijay",
    "password": "1612"
}
```

### Response

```json
{
    "message": "Admin login successful",
    "tokens": {
        "refresh": "refresh_token",
        "access": "access_token"
    }
}
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/Mr-Vijay16/Hostel-Management-System.git
```

---

## Create Virtual Environment

```bash
python -m venv env
```

---

## Activate Environment

### Windows

```bash
env\Scripts\activate
```

### Linux / Mac

```bash
source env/bin/activate
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

## Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Run Server

```bash
python manage.py runserver
```

---

# ☁️ Deployment

The project is deployed on **Render** using:
- Gunicorn
- WhiteNoise
- SQLite Database

---

# 👥 Team Members

| Name | Role |
|---|---|
| Vijay HS | Backend Development, APIs, Deployment |
| Jyothika | Room Management, Complaint Management, Fee Management |
| Jeevana Lalitha | Frontend/UI Design |
| Team Members | Testing & Documentation |

---

# 📈 Future Enhancements

- Hostel Attendance System
- Online Fee Payment
- Email Notifications
- Student Profile Photos
- Role-Based Access Control

---

# 👨‍💻 Author

## Vijay HS
- Full Stack Django Developer
- Python Developer

---

# ⭐ Support

If you like this project, give it a ⭐ on GitHub.
