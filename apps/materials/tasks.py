import smtplib
from calendar import monthrange
from datetime import datetime, timedelta

import pytz
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from apps.materials.models import Course
from apps.users.models.users import Users
from config.settings import EMAIL_HOST_USER


@shared_task
def check_user_activity():
    zone = pytz.timezone(settings.TIME_ZONE)
    now = datetime.now(zone)
    month = now.month
    year = now.year
    days_count = monthrange(year, month)
    expiration_date = now - timedelta(days=days_count[1])
    user_list = Users.objects.filter(last_login__lte=expiration_date, is_active=True)
    user_list.update(is_active=False)


@shared_task
def mailing_about_updates(course_id):
    course = Course.objects.get(pk=course_id)
    subscription_list = course.subscription.all()
    user_list = [subscription.user for subscription in subscription_list]
    try:
        response = send_mail(subject='Обновление курса',
                             message=f'Курс "{course}" обновился!',
                             from_email=EMAIL_HOST_USER,
                             recipient_list=user_list,
                             fail_silently=False,
                             )
        return response
    except smtplib.SMTPException as ex:
        raise ex
