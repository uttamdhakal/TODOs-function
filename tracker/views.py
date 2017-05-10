from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.views.generic import View
from .models import Todo
from django.http import HttpResponse
from django.template import loader
from django.core.urlresolvers import reverse_lazy


class IndexView(generic.ListView):
    template_name = 'tracker/index.html'
    context_object_name = 'all_todos' #default name = object_list

    def get_queryset(self):
        return Todo.objects.all()

class AlbumCreate(CreateView):
    model = Todo
    fields = ['description', 'status', 'deadline', 'assignee']

class AlbumUpdate(UpdateView):
    model = Todo
    fields = ['description', 'status', 'deadline', 'assignee']

class AlbumDelete(DeleteView):
    model = Todo
    success_url = reverse_lazy('tracker:index')
