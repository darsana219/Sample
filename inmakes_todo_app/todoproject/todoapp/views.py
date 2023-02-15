from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import Task
from .forms import TaskForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your class based views here.
class TaskListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'key'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'key'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'key'
    fields = ('name','priority','date')

    # creating link to get into update
    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.id})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')






# Create your function based views here.
def add(requset):
    task1 = Task.objects.all()
    if requset.method=='POST':
        name = requset.POST.get('task','')
        priority = requset.POST.get('priority','')
        date = requset.POST.get('date','')
        task = Task(name=name,priority=priority,date=date)
        task.save()
    return render(requset,'home.html',{'key':task1})

def delete(request,task_id):
    if request.method=='POST':
        task = Task.objects.get(id = task_id)
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,task_id):
    task = Task.objects.get(id=task_id)
    form = TaskForm(request.POST or None,instance = task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'task':task})

