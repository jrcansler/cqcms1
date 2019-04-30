from django import forms
from django.contrib.auth.models import User
#rom home.models import UserProfileInfo
from django.core import validators
from django.contrib.auth.models import User

class UserForm(forms.Form):
    first = forms.CharField(required=True)
    last = forms.CharField()
    company = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Verify Email: ')
    comment = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                    widget=forms.HiddenInput,
                                    validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError('verify email')
