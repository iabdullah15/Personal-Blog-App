from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse, HttpRequest

from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import login

# Create your views here.

def test(request):

    return render(request, 'home.html')


class Home(View):

    def get(self, request:HttpRequest):

        queryset = Post.objects.all().order_by('time_created')
        posts = {"posts": queryset}

        return render(request, 'home.html', posts)


class BlogPosts(ListView):

    template_name = 'posts.html'
    model = Post
    context_object_name = 'posts'
