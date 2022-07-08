from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render
from .models import ToDoListItem
from django.http import HttpResponseRedirect

# Create your views here.
def todoappView(request):
    allTodoItems = ToDoListItem.objects.all()
    return render(request, 'todolist.html',
    {'all_items': allTodoItems})

def addTodoView(request):
    x = request.POST['content']
    new_item = ToDoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/todoapp')

def deleteTodoView(request, i):
    y = ToDoListItem.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/todoapp/')