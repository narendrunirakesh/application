from django import forms

class SignUpForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    roles = forms.MultipleChoiceField(choices=[('Department Manager', 'Department Manager'), ('Store Manager', 'Store Manager')])

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
