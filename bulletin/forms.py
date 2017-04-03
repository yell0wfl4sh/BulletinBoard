from django import forms

class Login(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)

class Register(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(max_length=20)
	email = forms.EmailField()
	first_name = forms.CharField(max_length=20)
	last_name = forms.CharField(max_length=20)
	branch = forms.CharField()
	enr_no = forms.IntegerField()
