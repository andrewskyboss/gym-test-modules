from django import forms


class ContactUsForm(forms.Form):
    full_name = forms.CharField(max_length=150)
    email_address = forms.EmailField(max_length=150)
    message_field = forms.CharField(widget=forms.Textarea, max_length=2000)
