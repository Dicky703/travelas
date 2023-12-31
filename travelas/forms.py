from django import forms
from travelas.models import Page, Car 
from travelas.models import UserProfile
from django.contrib.auth.models import User


class CarForm(forms.ModelForm):
	name = forms.CharField(max_length = 128, help_text = "Please enter the car name.")
	views = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
	likes = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
 

	class Meta:
		model = Car

		fields = '__all__'

class PageForm(forms.ModelForm):
	title = forms.CharField(max_length = 128, help_text = "Please enter the title of the page.")
	url = forms.URLField(max_length = 200, help_text = "Please enter the URL of the page.")	
	views = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)

	class Meta:

		model = Page

		fields = ('title', 'url', 'views')

		def clean(self):
			cleaned_data = self.cleaned_data

			url = cleaned_data.get('url')

			if url and not url.startswith('http://'):
				url = 'http://' + url
				cleaned_data['url'] = url

				return cleaned_data	

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')				