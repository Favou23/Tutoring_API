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
* Configure Django REST Framework for Authentication API
* Use Celery for asynchronous operations in Django REST Framework
* Understand JWT authentication (Access & Refresh tokens)
* use `.env` files for secret environment variable management

---

## Introduction
This is not just code it’s a **learning project**.  

The project demonstrates how to:
* Integrate Celery asynchronous processes into Django rest framework
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

---

#### 2.  JWT Authentication
JWT, which stands for JSON Web Token, is a compact, stateless mechanism for API authentication. When a user logs into an application, the API server creates a digitally signed and encrypted JWT that includes the user's identity. The client then includes the JWT in every subsequent request, which the server deserializes and validates. The user's data is therefore not stored on the server's side, which improves scalability.

* file:`settings.py`
   ```python
    SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    }
    ```

### 3. Database configuration 
For this project, **PostgreSQL** is used instead of the default SQLite.  
First, install the PostgreSQL driver:
```python
pip install psycopg2
```
In settings.py, update the DATABASES configuration to load sensitive values from the **.env** file:
* file: `settings.py`
   ```python
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
   }
   ```
After configuring the database, generate and apply migrations:
```python
 python makemigrations
 python migrate
 ```