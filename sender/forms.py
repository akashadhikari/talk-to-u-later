from django import forms


class MessageForm(forms.Form):
    my_facebook_email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your Facebook email.'
    }))
    my_facebook_password = forms.CharField(
        help_text='<b>NOTE: The creator of this app <code>does not</code> acquire your login credentials by <code>any</code> means. Security and privacy are pretty serious deals form him!</b>',
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
