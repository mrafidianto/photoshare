from django.shortcuts import render, redirect
from django.forms import ModelForm
from django import forms
from .models import Post

# Create your views here.
def home_view(request):
    title = "Welcome to PhotoShare!"
    posts = Post.objects.all()
    return render(request, 'a_posts/home.html', {'title': title, 'posts': posts})

class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'body']

def post_create_view(request):
    
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    
    return render(request, 'a_posts/post_create.html')