from django.urls import path
from .views import send_message, sent


app_name = 'sender'
urlpatterns = [
    path('', send_message, name='send_message'),
    path('sent', sent, name='sent')
]
