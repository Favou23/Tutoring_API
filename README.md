# Tutoring_API
DRF based Authorization API for an online tutoring platform.


![Django REST API](/logo.svg)

<div align="center">
  <h1>Django REST Framework – JWT Authentication API</h1>
</div>

<div align="center">
  <strong>Learn Django REST Framework by building a JWT-based authentication system</strong>
</div>

<div align="center">
  This project is a step-by-step implementation of an authentication backend using Django, Django REST Framework, and SimpleJWT.
</div>

<br>

<div align="center">
  Please join the community: <br>
  <a href="#">Website (Coming Soon)</a>
  <span> | </span>
  <a href="https://www.djangoproject.com/">Django</a>
  <span> | </span>
  <a href="https://www.django-rest-framework.org/">DRF</a>
</div>

---

## 🎯 Aims of this Project
The aims of this project are to:
* Learn how to configure Django REST Framework
* Understand JWT authentication (Access & Refresh tokens)
* Learn how to use `.env` files for secret management
* Provide reusable authentication boilerplate for other projects

---

## 📖 Project Introduction
This is not just code — it’s a **learning project**.  

The project demonstrates how to:
* Build a **custom user model** that uses email instead of username
* Configure **JWT authentication**
* Securely manage secrets using **dotenv**
* Create and test **authentication endpoints** with Postman or cURL  

The documentation also explains the **process I followed** to build it step by step.

---

## 🛠 Process & Implementation

### 1. Setting up Django & DRF
- Installed Django and DRF
- Created a project and app
- Added `rest_framework` and `rest_framework_simplejwt` to `INSTALLED_APPS`

### 2. Creating a Custom User Model
File: `models.py`
```python
from django.db import models
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser):
    email = models.EmailField(max_length=200, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
