from django.db import models
import datetime 
# Create your models here.
class Task(models.Model):
#accept object itself to display the name of the task
	def __str__(self):
		return self.name
	#name of the task	
	name = models.CharField(max_length=100)
	#interger field,priority is a number
	priority = models.IntegerField()
	#To display date and time
	#The default it to automatically update the current date
	date = models.DateField(default=datetime.date.today)
	