#  i first created a virtual environment  and activated it 
#  then i pip installed django, djangorestframework, djangorestframework-simplejwt, celery redis
#  then i created a django project called tutoring_api
#  then i created an app called accounts
#  then i added the app and the rest_framework and the simplejwt to the installed apps 
# then i added the rest_framework settings for the simplejwt authentication
#  THEN I CONFIGURED THE DATABASE TO USE POSTGRESQL INSTEAD OF SQLITE3
# then i created a .env file in the base director and added the database credentials there
# then i used python-dotenv to load the .env file in the settings.py
# then i also used the python dot-env to load the secret key from the .env file
# then i configured the simplejwt settings to have access token lifetime of 15 minutes and refresh token lifetime of 1 day
# then i added the celery settings to the .env file and also in the settings.py file
# then i created the user classin the accounts model file 
# then i created a seriaizer file where i class register  serializer and added the validation for the password field and also creation
# then i created the views for the register and logout
# then i created the urls for the accounts app and included them in the main urls.py file
# then i configures the postgres database and created the migrations and migrated
# then i created a celery.py file in the base directory and configured the celery settings there
# then i created a tasks.py file in the accounts app and created a sample task to send email
# then i ran the server and the celery worker and tested the api using postman