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
@shared_task
def send_password_reset_success_email(user_email):
    subject = "Your password was reset successfully"
    message = (
        "Hello,\n\n"
        "Your password has been reset successfully. "
        "If you did not perform this action, please contact support immediately."
    )
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user_email],
        fail_silently=False,
    )
@shared_task
def send_password_reset_email(user_email, reset_link):
    send_mail(
        "Password Reset Request",
        (f"click the link to reset your password: {reset_link}"),
        "noreply@tutoringapp.com",
        [user_email],
        fail_silently=False,
    )
    return "Email sent"

@shared_task
def send_account_deletion_email(user_email):
    send_mail(
        "Account Deletion Confirmation",
        "Your account has been successfully deleted.",
        "noreply@tutoringapp.com",
        [user_email],
        fail_silently=False,
    )
    return "Email sent"

@shared_task
def send_profile_update_email(user_email):
    send_mail(
        "Profile Updated",
        "Your profile information has been successfully updated.",
        "noreply@tutoringapp.com",
        [user_email],
        fail_silently=False,
    )
    return "Email sent"



# (venv) PS C:\Users\USER\Desktop\my_first_api> celery -A tutoring_api worker --pool=solo -l info
   
#  -------------- celery@DESKTOP-KI96D30 v5.5.3 (immunity)
# --- ***** ----- 
# -- ******* ---- Windows-11-10.0.22631-SP0 2025-09-23 05:07:41
# - *** --- * --- 
# - ** ---------- [config]
# - ** ---------- .> app:         tutoring_api:0x1a0652b1760
# - ** ---------- .> transport:   redis://localhost:6379/0
# - ** ---------- .> results:     redis://localhost:6379/0
# - *** --- * --- .> concurrency: 8 (solo)
# -- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
# --- ***** ----- 
#  -------------- [queues]
#                 .> celery           exchange=celery(direct) key=celery


# [tasks]
#   . accounts.tasks.send_account_deletion_email
#   . accounts.tasks.send_password_reset_email
#   . accounts.tasks.send_profile_update_email
#   . accounts.tasks.send_welcome_email

# [2025-09-23 05:07:43,734: INFO/MainProcess] Connected to redis://localhost:6379/0
# [2025-09-23 05:07:45,774: INFO/MainProcess] mingle: searching for neighbors
# [2025-09-23 05:07:52,941: INFO/MainProcess] mingle: all alone
# [2025-09-23 05:08:03,131: INFO/MainProcess] celery@DESKTOP-KI96D30 ready
