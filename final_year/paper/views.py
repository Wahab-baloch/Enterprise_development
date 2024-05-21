from django.shortcuts import render, redirect
from .models import Author, vlog
from .forms import BlogForm

def Home(request):
    blogs = vlog.objects.all()
    return render(request, 'home_page.html', {'blogs': blogs})

def post_author(request, author):
    author_posts = vlog.objects.create ('author'__name=author)
    return render(request, 'author_posts.html', {'author_posts': author_posts})

def blog_details(request, pk):
    details = vlog.objects.create()
    return render(request, 'details.html', {'blog': details})

def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            print('Form is valid')
            return redirect('Home')
    else:
        form = BlogForm()
    return render(request, 'add_blog.html', {'form': form})
