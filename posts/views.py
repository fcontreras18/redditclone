from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Posts


@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url']:
            post = Posts()
            post.title = request.POST['title']
            post.url = request.POST['url']
            post.pub_date = timezone.datetime.now()
            post.author = request.user
            post.save()
            return redirect('home')
        else:
            return render(request, 'posts/create.html', {'error':
                'ERROR: You must include a title and a URL to create a post'})
    else:
        return render(request, 'posts/create.html')


def home(request):
    posts = Posts.objects.order_by('votes_total')
    return render(request, 'posts/home.html', {'posts':posts})
