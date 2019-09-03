import os
from decouple import config
from django import forms
from django.core.mail import EmailMultiAlternatives
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import From, To, Personalization, Mail


try:
    # Python 3
    import urllib.request as urllib
except ImportError:
    # Python 2
    import urllib2 as urllib


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

        # Issue response to client via sendgrid API
        sendgrid_client = SendGridAPIClient(config('SENDGRID_API_KEY'))
        mail = Mail()
        mail.from_email = From(config('EMAIL_FROM'))
        mail.to_email = To(email)
        mail.subject = "Your Enquiry with Mayan Web Studio"
        mail.template_id = config('SENDGRID_TEMPLATE_ID')
        p = Personalization()
        p.add_to(To(email))
        p.dynamic_template_data = {
            "firstName": first_name,
            "lastName": last_name,
            "phone": phone
        }
        mail.add_personalization(p)

        response = sendgrid_client.client.mail.send.post(
            request_body=mail.get())
        print(response.status_code)
        print(response.body)
        print(response.headers)

        # Send notification email to Mayan
        subject, from_email, to = 'New Enquiry for Mayan Web Studio', config(
            'EMAIL_FROM'), 'mike@mayanwebstudio.co.uk'
        text_content = 'This is an important message.'
        html_content = '''
        <h3>New Enquiry from</h3>
        <ul>
        <li>First Name: $(first_name)</li>
        <li>Last Name: $(last_name)</li>
        <li>Email: $(email)</li>
        <li>Phone: $(phone)</li>
        <li>Message: $(message)</li>
        </ul>
        '''

        html_content = html_content.replace("$(first_name)", first_name)
        html_content = html_content.replace("$(last_name)", last_name)
        html_content = html_content.replace("$(email)", email)
        html_content = html_content.replace("$(phone)", phone)
        html_content = html_content.replace("$(message)", message)

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    # from_email = Email(config('EMAIL_FROM'), 'Mayan Web Studio')
    # to_email = email

    # mail = Mail(from_email, to_email)
    # mail.personalizations[0].add_substitution(
    #     Substitution("-firstName-", first_name))
    # mail.personalizations[0].add_substitution(
    #     Substitution("-lastName-", last_name))
    # mail.personalizations[0].add_substitution(
    #     Substitution("-phone-", phone))
    # mail.template_id = config('SENDGRID_TEMPLATE_ID')

    # data = {
    #     "asm": {
    #         "group_id": 13815,
    #     },
    #     "content": [
    #         {
    #             "type": "text/html",
    #             "value": "<html><p>Hello from Mayan</p></html>"
    #         }
    #     ],
    #     "from": {
    #         "email": config('EMAIL_FROM'),
    #         "name": "Mayan Web Studio"
    #     },
    #     "personalizations": [
    #         {
    #             "headers": {
    #                 "X-Accept-Language": "en",
    #                 "X-Mailer": "MyApp"
    #             },
    #             "subject": "Your Enquiry with Mayan Web Studio",
    #             "substitutions": {
    #                 "firstName": first_name,
    #                 "lastName": last_name,
    #                 "phone": phone
    #             },
    #             "to": [
    #                 {
    #                     "email": email,
    #                     "name": "Mayan Web Studio"
    #                 }
    #             ]
    #         }
    #     ],
    #     "reply_to": {
    #         "email": "hello@mayanwebstudio.co.uk",
    #         "name": "Mayan Web Studio"
    #     },
    #     "template_id": config('SENDGRID_TEMPLATE_ID')
    # }

    #     message = Mail(
    #         from_email=config('EMAIL_FROM'),
    #         to_emails=config('EMAIL_TO'),
    #         html_content=)

    #     try:
    #         sendgrid_client = SendGridAPIClient(config('SENDGRID_API_KEY'))
    #         response = sendgrid_client.send(message)
    #         print(response.status_code)
    #         print(response.body)
    #         print(response.headers)
    #     except Exception as e:
    #         print(e)
