import datetime

from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from .forms import CreateForm, UpdateForm
from datetime import datetime

class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"
    template_name = "posts/index.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)


class BlogCreate(CreateView):
    form_class = CreateForm
    template_name = "posts/create.html"


class BlogUpdate(UpdateView):
    model = BlogPost
    form_class = UpdateForm
    template_name = "posts/edit.html"


class BlogDetail(DetailView):
    model = BlogPost
    context_object_name = "posts"
    template_name = "posts/detail.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)


class BlogDelete(DeleteView):
    model = BlogPost
    template_name = "posts/delete.html"
    success_url = reverse_lazy("posts:home")