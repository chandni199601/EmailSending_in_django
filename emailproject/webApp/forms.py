from django import forms
class SendForm(forms.Form):
    name=forms.CharField(max_length=80,)
    email=forms.CharField(max_length=80)
    subject=forms.CharField(max_length=80)
    message=forms.CharField(required=False)
