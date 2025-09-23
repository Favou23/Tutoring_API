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
* Learn how to configure Django REST Framework for Aute
* Use Celery for asynchronous operations in Django REST Framework
* Understand JWT authentication (Access & Refresh tokens)
* use `.env` files for secret management

---

## Project Introduction
This is not just code it’s a **learning project**.  

The project demonstrates how to:
* Imtegrate Celery asynchronous processes into Django rest framework
* Configure **JWT authentication**
* Securely manage secrets using **dotenv**
* Create and test **authentication endpoints** with Postman  

The documentation also explains the **process I followed** to build it step by step.

---

##  Process & Implementation
### 1. Setting up Django & DRF
- Installed Django and DRF
  ```python
  pip install django djangorestframework rest_framework_simplejwt
  ```
  
- Created a project and app
  ```python
  django-admin createproject tutoring_api
  py manage.py startapp accounts
  ```
  
- Added the **`installed app`** and the **`rest_frameork`** and its associates to the settings.py file
 ```python 
 
 REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    )
  }

 INSTALLED_APPS = [
    
  'rest_framework',
  'rest_framework_simplejwt.token_blacklist',
  "rest_framework_simplejwt",
  'accounts',
 ]
 ```

#### 2. Configuring the JWT Authentication
 ```python
  SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
  }
  ```