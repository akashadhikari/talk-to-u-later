import celery
from fbchat.models import *
from django.http import HttpResponse


@celery.task()
def send_delay_user(client, message, thread_id):
    client.send(Message(text=message), thread_id=thread_id, thread_type=ThreadType.USER)
    return HttpResponse('Message Sent Successfully')

@celery.task()
def send_delay_group(client, message, thread_id):
    client.send(Message(text=message), thread_id=thread_id, thread_type=ThreadType.GROUP)
    return HttpResponse('Message Sent Successfully')
