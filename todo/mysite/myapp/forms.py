from .models import Task
from django import forms

#create a model form for to todo list application
#Model form inheritant from the modelform
class TodoForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['name','priority','date']