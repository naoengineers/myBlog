from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

def index(request):
    posts = Post.objects.order_by('-published')
    return render(request, 'posts/index.html', {'posts': posts})

def post_detail(request, post_id):
    # pkに合致するデータを Post オブジェクトから取得し、ない場合は、404(Not Found)を返す
    post = get_object_or_404(Post, pk=post_id)

    # pkに合致するデータを Post オブジェクトから取得するのみ。
    # post = Post.objects.get(pk=post_id)
    return render(request, 'posts/post_detail.html', {'post':post})