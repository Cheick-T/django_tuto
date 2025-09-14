from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post
from .form import CreatePostForm

# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request,'posts/posts_list.html', {'posts': posts})


def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    #return HttpResponse(slug)
    return render(request,'posts/post_page.html', {'post': post})

@login_required(login_url='/users/login')
def new_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            #return render(request,'posts/post_page.html', {'post': post})
            return redirect('posts:list')
    else:
        form = CreatePostForm()
    return render(request,'posts/new_post.html', {'form': form})