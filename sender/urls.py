from django.conf.urls import url
from .views import send_message, sent


app_name = 'sender'
urlpatterns = [
    url(r'^', send_message, name='send_message'),
    url(r'^sent/$', sent, name='sent'),
]
