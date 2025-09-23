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
* Integrate Celery asynchronous process into Django rest framework
* Configure **JWT authentication**
* Securely manage secrets using **dotenv**
* Create and test **authentication endpoints** with Postman  

This documentation also explains the **process I followed** to build it step by step.

---

##  Process & Implementation
### 1. Setting up Django & DRF
- Installed Django and DRF
  ```python
  pip install django djangorestframework rest_framework_simplejwt Celery Redis
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
* First, install the PostgreSQL driver:
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

        SECRET_KEY = os.getenv("SECRET_KEY")
    }
   }
   ```
After configuring the database, generate and apply migrations:
```python
 python manage.py makemigrations
 python manage.py migrate
 ```
## 4. Celery, redis and background task processing 
* `why Celery?`
* In this project, some tasks (like sending emails, processing notifications, refreshing tokens, or heavy computations) should not block the main API response.
If the API tried to do everything immediately (synchronously), users would wait a long time before receiving a response.
**Celery** is used as a background task queue that lets us offload time-consuming operations so the API can remain fast and responsive.`
#### Role of redis
Celery needs a “broker” **(a message transport system)** to pass messages between the API and the Celery workers.
* In this project, Redis is used as the message broker and result backend.
* When the API receives a request that triggers a background task **(e.g., registration email),** the task is converted into a JSON message and pushed to Redis.
* A Celery worker (running in the background) listens for new messages in Redis, pulls them, executes the task, and stores the result.
## 5. JSON Messages Flow (on POST Request)
Here’s what happens step by step when a client sends a POST request (registration or login):

* A user sends a request (POST /api/register) with JSON payload.

```python
  {
    "username": "newuser",
    "email": "example@gmail.com",
    "password": "securepassword123"
  }
  ```

* Django REST Framework handles the request and saves the user (synchronously).
* At the same time, a background task is scheduled **(send welcome email).**
* Celery serializes the task into a JSON message:
```python
{
  "task": "send_welcome_email",
  "args": ["user@example.com"],
  "kwargs": {},
  "id": "c9d72a23-89f9-4f77-9d35-6c47c12e8e3a"
}
```
* This message is published to Redis and waits in a queue.
* A worker picks up the message, runs the send_welcome_email function, and completes the task asynchronously.
* The client immediately receives a success response (without waiting for email sending).

### tasks.py
* Example Task (Email Sending):
```python
from celery import shared_task
from django.core.mail import send_mail

Email = "tutoringteam@gmail.com"

@shared_task
def send_welcome_email(user_email, username):
    send_mail(
        (f'welcome to the Tutoring app {username}'),
        ("You have taken a bold step in your learning journey, we wish you the bset of luck")
        (Email)
        [user_email],
        fail_silently=False,
    )