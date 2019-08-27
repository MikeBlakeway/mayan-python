from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput, label="Name", error_messages={
                           'required': 'Please enter your name'}, required=True)
    email = forms.EmailField()
    phone = forms.CharField(widget=forms.TextInput, label="Phone", error_messages={
                            'required': 'Please enter your contact number'}, required=True)
    message = forms.CharField(widget=forms.Textarea,
                              label="Message", required=False)

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
