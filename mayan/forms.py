import os
from decouple import config
from django import forms
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


# TODO: integrate email responder

class ContactForm(forms.Form):

    fname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': False,
            }
        ),
        max_length=80,
        required=True,
        error_messages={'required': 'Please enter your first name'},
    )

    lname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': False,
            }
        ),
        max_length=80,
        required=True,
        error_messages={'required': 'Please enter your last name'},
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'id': False,
            }
        ),
        label='',
        max_length=80,
        required=True,
        error_messages={
            'required': 'Please enter your email address',
            'invalid': 'Please enter a valid email address'
        },
    )

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': False,
            }
        ),
        label='',
        max_length=80,
        required=True,
        error_messages={'required': 'Please enter your contact number'},
    )

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': '3',
                'cols': '40',
                'id': False,
                'autofocus': True
            }
        ),
        label='',
        required=False,
    )

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        first_name = self.cleaned_data.get("fname")
        last_name = self.cleaned_data.get("lname")
        email = self.cleaned_data.get("email")
        phone = self.cleaned_data.get("phone")
        message = self.cleaned_data.get("message")

        message = Mail(
            from_email=config('EMAIL_FROM'),
            to_emails=config('EMAIL_TO'),
            subject='Sending with Twilio SendGrid is Fun',
            html_content='<strong>and easy to do anywhere, even with Python</strong>'
        )

        try:
            sg = SendGridAPIClient(config('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)
