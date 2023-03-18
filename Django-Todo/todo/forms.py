from django import forms
from django.forms import ModelForm
from .models import *

class CreateForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))

	class Meta:
		model = Create
		fields = '__all__'