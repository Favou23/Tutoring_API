
FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV DJANGO_SETTINGS_MODULE=tutoring_api.settings
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8080
CMD python manage.py migrate && \
    gunicorn --bind 0.0.0.0:8080 --workers 4 --timeout 120 tutoring_api.wsgi:application
