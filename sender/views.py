import json
from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from django.http import HttpResponse
from fbchat import Client
from fbchat.models import *

from .forms import MessageForm
from .tasks import send_delay_user, send_delay_group


def send_message(request):
    form = MessageForm(request.POST or None)
    context = {
        "page_title": "Send quick message.",
        "form": form
    }
    if form.is_valid():

        email = request.POST.get('my_facebook_email')
        password = request.POST.get('my_facebook_password')

        thread_type = request.POST.get('message_target')
        thread_id = request.POST.get('thread_id')
        message = request.POST.get('my_message')
        schedule_time = request.POST.get('schedule_time')
        now = datetime.now()
        striped_date = datetime.strptime(schedule_time, '%Y-%m-%d %H:%M:%S')
        total_seconds = (striped_date - now).total_seconds()
        if total_seconds < 0:
            total_seconds = 0

        client = Client(email, password)

        if thread_type == 'ThreadType.GROUP':
            send_delay_group.apply_async(args=[client, message, thread_id], eta=datetime.utcnow() + timedelta(seconds=total_seconds))
        else:
            send_delay_user.apply_async(args=[client, message, thread_id], eta=datetime.utcnow() + timedelta(seconds=total_seconds))
    if request.POST:
        return HttpResponse("<b>SUCCESS!!! </b>Message Sent To Queue. <a href='/'>Send again?</a>")

    return render(request, "send/send_message.html", context)


def sent(request):
    context = {
        "page_title": "Success",
    }
    return render(request, "send/sent.html", context)

# celery -A ttyl worker -l info
# celery -A ttyl beat -l info
