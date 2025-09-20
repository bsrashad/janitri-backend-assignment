# Janitri Backend Assignment

A Django REST Framework project for managing **Users, Patients, and Heart Rate Data**.  
Implements authentication (JWT), CRUD operations, validations, and unit tests.

🚀 Tech Stack

Python 3.11+
Django 5.2.6
Django REST Framework
JWT Authentication (djangorestframework-simplejwt)
drf-spectacular (for API docs)
MySQL (database)
---

## 🚀 Features
- **User Authentication** (JWT-based login & registration)
- **Patient Management**
  - Create a patient
  - List patients (only for the logged-in user)
- **Heart Rate Data**
  - Add heart rate data for a patient
  - List heart rate data (with pagination & ordering by timestamp)
- **Validation**
  - Age must be greater than 0
  - Heart rate must be between 30–250 bpm
- **Unit Tests** for all major APIs
- **Swagger API Docs** via drf-yasg

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/bsrashad/janitri-backend-assignment.git
cd janitri-backend-assignment

2. Create & activate virtual environment
python -m venv venv
# On Windows
venv\Scripts\activate
# On Linux/Mac
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Configure Database

Update janitri_backend/settings.py with your MySQL credentials:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'janitri_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

5️. Run migrations
python manage.py makemigrations
python manage.py migrate

6 . Run server
python manage.py runserver


🔑 Authentication

This project uses JWT Authentication.

Obtain token: POST /api/users/login/

Refresh token: POST /api/token/refresh/

Use the token in headers:

Authorization: Bearer <your_access_token>

📖 API Documentation

Once the server is running:

Swagger UI → http://localhost:8000/api/schema/swagger-ui/

===
Running Tests
python manage.py test patients


====

API Endpoints
🔹 Users

POST /api/users/register/ → Register new user

POST /api/users/login/ → Login & get JWT tokens

POST /api/token/refresh/ → Refresh token

🔹 Patients

GET /api/patients/ → List logged-in user’s patients

POST /api/patients/add/ → Create new patient

🔹 Heart Rate Data

GET /api/patients/heart-rate/<patient_id>/ → List patient’s heart rate data

POST /api/patients/heart-rate/add/ → Add new heart rate entry

==========
Assumptions & Decisions

Each patient is linked to the logged-in user (multi-user system).

Heart rate range validation: must be between 30 and 250 bpm.

Age validation: must be greater than 0.

Default pagination: 10 items per page.

Authentication required for all endpoints.