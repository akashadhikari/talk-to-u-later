from datetime import datetime
from django import forms


class MessageForm(forms.Form):
    my_facebook_email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your Facebook email.'
    }))
    my_facebook_password = forms.CharField(
        help_text='<b>NOTE: The creator of this app <code>does not</code> acquire your login credentials by <code>any</code> means. Security and privacy are pretty serious deals for him!</b>',
        widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your Facebook password.'
    }))
    TARGET = (
        ('ThreadType.USER', 'User'),
        ('ThreadType.GROUP', 'Group')
    )

    message_target = forms.ChoiceField(choices=TARGET,
        label="Message Target",
        required=True,
        initial='',
        widget=forms.Select(attrs={
            'class': 'form-control',
            }))
    thread_id = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'The thread ID of a person or a group that you want to send the message.'
    }))
    my_message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Write your message.',
        'rows': 4,
        'cols': 15
    }))
    schedule_time = forms.DateTimeField(
        required = False,
        input_formats=["%Y-%m-%d %H:%M:%S"],
        initial=datetime.strptime(str(datetime.now())[:-7], '%Y-%m-%d %H:%M:%S'),
        help_text='<b>Note:</b> Leaving this field <b>as is</b> will send the message right NOW. Also, if you insert past time, the system will automatically make it to present.',
        widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Should be something like: 2020-05-35 01:30:20',

    }))
