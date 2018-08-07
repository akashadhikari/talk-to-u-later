import celery
from django.http import HttpResponse


@celery.task()
def send_messages(users_devices, message):
    users_devices.send_message(title='message', body=message)
    return HttpResponse('Message Send Successfully')