from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BlogPostForm
 

def index(request):
    return render(request, 'homepage/index.html')

def admin(request):
    return render(request, 'admin/admin.html')


def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the data to the database
            return redirect('/')  # Redirect to a success page after submission
    else:
        form = BlogPostForm()

    return render(request, 'admin/admin.html', {'form': form})


def view_blog_posts(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'homepage/index.html', {'blog_posts': blog_posts})