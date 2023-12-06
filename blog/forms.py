from django.forms import Form, CharField, EmailField, PasswordInput


class SignupForm(Form):
    first_name = CharField(label="First name", max_length=20)
    last_name = CharField(label="Last name", max_length=20)
    email = EmailField(label="Email Address")
    password = CharField(label="Password", widget=PasswordInput)
    
class LoginForm(Form):
    email = EmailField(label="Email Address")
    password = CharField(label="Password", widget=PasswordInput)