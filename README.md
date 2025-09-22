<div align="center">
  <h1>Tutoring_app Authentication and Authorization API</h1>
</div>

<div align="center">
  This project is a step-by-step implementation of an authentication backend using Django, Django REST Framework, Celery and SimpleJWT.
</div>

<br>


---

##  Aims of this Project
The aims of this project are to:
* Learn how to configure Django REST Framework
* Use Celery for asynchronous operations in Django REST Framework
* Understand JWT authentication (Access & Refresh tokens)
* Learn how to use `.env` files for secret management

---

## Project Introduction
This is not just code it’s a **learning project**.  

The project demonstrates how to:
* Build a **custom user model** that uses email instead of username
* Configure **JWT authentication**
* Securely manage secrets using **dotenv**
* Create and test **authentication endpoints** with Postman  

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
