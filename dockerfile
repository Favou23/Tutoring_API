
FROM python:3.12.1-slim
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /app
COPY . .
RUN pip instal --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD [ "python","manage.py", "runserver" ]
