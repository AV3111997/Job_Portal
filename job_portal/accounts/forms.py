from django import forms

class PasswordConfirmationForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'autocomplete':'current-password',
        'placeholder': 'password'
        }),label="Please enter your login Password to confirm:")

