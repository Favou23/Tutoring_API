## THIS FILE CONTAINS THE STEP BY STEP PROCESSES TO RUN THIS DOCKERIZED PROJECT 
--
### STEP 1: 
* In Your terminal console use the command below to clone the repository into your machine
```sh
 git clone <"repository_url">
```
### STEP 2:
* navigate to the cloned project directory
```sh
 cd "project_directory"
```
### STEP 3:
* in the root project directory, create a **.env** file for configuring and storing your environment variables and open the file for encironment variables configuration

### STEP 4:
* CONFIGURE THE ENVIRONMENT VARIABLES WITH THE FORMAT BELOW:
```sh
SECRET_KEY= "your_secret_key"


DB_NAME=your_db_name
DB_USER=username
DB_PASSWORD=password
DB_HOST=db #unchanged 
DB_PORT=5432 #unchanged



CELERY_BROKER_URL= 'redis://redis:6379/0' #unchanged
CELERY_RESULTS_BACKEND= 'redis://redis:6379/0' #unchanged
```
## step 5:
* RUN THE DOCKER COMMAND TO BUILD THE IMAGES AND SPIN UP THE CONTAINERS AFTER BUILDING
```sh
 docker-compose up --build
 # YOU SHOULD SEE THE PROJECT RUNNING IN YOUR MACHINE LOCALHOST SERVER "http://localhost:8000"
```
* FOR SUBSEQUENT SPINNING UP OF THE CONTAINER, RUN THE COMMAND BELOW:
```sh
 docker-compose up
```
## STEP 6:
* **TESTING THE ENDPOINTS OF THE API's**
=====> to test the registeration endpoint on your localhost server input the url below:
```sh
 http://localhost:8000/api/register/
```
=====> to test the login endpoint, input the url below:
```sh
 http://localhost:8000/api/login/
```
=====> to test the logout endpoint,use the url below and also copy the refresh token from the login session for proper logging out and  blacklisting of the token
```sh
 http://localhost:8000/api/logout/
```
=====> To test the reset-password endpoint, use the url below:
```sh
http://localhost:8000/api/reest-password/
```
---
**AFTER REQUESTING PASSWORD RESET WITH THE LINK ABOVE, A RESET LINK WOULD BE SENT TO THE USER, USUALLY THE TERMINAL CONSOLE AT THE DEVELOPMENT STAGE**
**THEN CLICK ON THE LINK, YOULL BE REDIRECTED TO THE PASSWORD RESET PAGE**
====> To test the reset-password-confirm endpoint, below is the url that the clicked link will redirected to 
```sh
"/api/reset-password-confirm/MQ/cwohnr-3dc912ef3412900a24087b874c26cc75/"
```
* then type  in the new password to confirm the password reset 