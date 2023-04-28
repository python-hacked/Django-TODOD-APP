from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateForm
from django.views.generic import CreateView
from django.views.generic import ListView
from .models import Create
from django.views.generic import UpdateView
from django.views.generic import DeleteView

# Create your views here.


class index(CreateView):
    model = Create
    form_class = CreateForm
    template_name = "todo/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        return context


class update(UpdateView):
    model = Create
    template_name = 'todo/update.html'
    success_url = "/"
    fields = {
        "title",
        "complete"
    }


class delete(DeleteView):
    model = Create
    success_url = "/"
    template_name = 'todo/delete.html'
