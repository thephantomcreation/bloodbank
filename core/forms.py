from django import forms
from .models import Blood

class ContactForm(forms.Form):
	name = forms.CharField(label="",
			widget=forms.TextInput(attrs={
				"name" : "name",
			    "placeholder" : "Name"
				})
		)
	email = forms.EmailField(label="",
			widget=forms.EmailInput(attrs={
				"name" : "email",
				"placeholder" : "Email"

				})
		)
	message = forms.CharField(label="",
			widget=forms.Textarea(attrs={
				 "name" : "message",
				 "placeholder" : "Your message"
				})
		)

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if not "gmail.com" in email and  not "yahoo.com" in email and not "hotmail.com" in email:
			raise forms.ValidationError("Please use gmail/yahoo/hotmail email address")
		return email

