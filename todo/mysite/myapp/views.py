from django.shortcuts import render,redirect
from .models import Task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
#display list of items
class TaskListView(ListView):
	#make use of the model
	model = Task
	template_name = 'myapp/index.html'
	#pass context object
	context_object_name = 'task_list'

class TaskDetailView(DetailView):
	model= Task
	template_name = 'myapp/detail.html'
	context_object_name = 'task'

class TaskUpdateView(UpdateView):
	model = Task
	template_name = 'myapp/update.html'
	context_object_name = 'task'
	fields = ('name','priority','date')
#to return to the detail view of the item we edited
	def get_success_url(self):
		#pk is the primary key
		#to define success url
		#kwargs keywords argument
		return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
	model= Task
	template_name = 'myapp/delete.html'
	success_url = reverse_lazy('cbvindex')
	context_object_name = 'task'


def index(request):
	#to get all the task from the Task model
	task_list = Task.objects.all()
	#check the request method is equals to POST
	if request.method=="POST":
		name = request.POST.get('name','')
		priority = request.POST.get('priority','')
		#to get the date
		date = request.POST.get('date','')
		#create and object to save the data to database
		#pass thje date to the task
		task = Task(name=name,priority=priority,date=date)
		task.save()
		#redirect the user to the homepage /=homepage
		return redirect('/')

	#Pass the object to a specific template
	return render(request,'myapp/index.html',{'task_list':task_list})

def delete(request,taskid):
	task = Task.objects.get(id=taskid)
	#handle the delete function after the submit button is clicked
	if request.method=="POST":
		#execute the task we want
		task.delete()
		#return to the Homepage
		return redirect('/')
		#delete.html is the template which contains delete functions
	return render(request,'myapp/delete.html',{'task':task})


def update(request,id):
	task = Task.objects.get(id=id)
	form = TodoForm(request.POST or None, instance=task)
	#check the validity of the form
	if form.is_valid():
		form.save()
		#return to homepage
		return redirect('/')
	return render(request,'myapp/edit.html',{'form':form,'task':task})
	#design template at edit.html