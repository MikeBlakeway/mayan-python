from django import forms


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
        error_messages={'required': 'Please enter a valid email'},
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

        print(
            first_name,
            last_name,
            email,
            phone,
            message
        )
