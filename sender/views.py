from django.shortcuts import render, redirect
from fbchat import Client
from fbchat.models import *

from .forms import MessageForm


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

    
        client = Client(email, password)

        if thread_type == 'ThreadType.GROUP':
            client.send(Message(text=message), thread_id=thread_id, thread_type=ThreadType.GROUP)
        else:
            client.send(Message(text=message), thread_id=thread_id, thread_type=ThreadType.USER)
    if request.POST:
        return redirect('sender:sent')

    return render(request, "send/send_message.html", context)


def sent(request):
    context = {
        "page_title": "Success",
    }
    return render(request, "send/sent.html", context)