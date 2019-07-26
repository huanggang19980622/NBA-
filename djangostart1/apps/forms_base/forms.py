from django import forms
class ContactForm(forms.Form):
    subject = forms.CharField()
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField()