from django import forms


class ContactUsForm(forms.Form):
    full_name = forms.CharField(max_length=150)
    email_address = forms.EmailField(max_length=150)
    message_field = forms.CharField(widget=forms.Textarea, max_length=2000)

    def __init__(self, *args, **kwargs):
        super(ContactUsForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].label = "Full Name:"
        self.fields['email_address'].label = "Email:"
        self.fields['message_field'].label = "Message:"
