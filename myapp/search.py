from myapp.models import Blog, Category, Comment
from django.db.models import Q, Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse 
from django.contrib import messages

def search(request):
        
    if request.method == 'GET':
        search = request.GET.get('search')

        search_comment = Blog.objects.filter(Q(title__icontains = search) | Q(description__icontains = search)) if search else None
        return search_comment

def popular_post(request):
    blog = Blog.objects.all()
     # Annotate each blog with the count of comments
    blog_with_comment_count = blog.annotate(comment_count=Count('comment'))

    # Group the blog posts by comment count
    grouped_blogs = {}
    for blog_post in blog_with_comment_count:
        comment_count = blog_post.comment_count
        if comment_count not in grouped_blogs:
            grouped_blogs[comment_count] = []
        grouped_blogs[comment_count].append(blog_post)

    # Select the top posts from each group
    popular_posts = []
    for comment_count, posts in sorted(grouped_blogs.items(), reverse=True):
        popular_posts.extend(posts[:3])

    return popular_posts


def pagination(request, blog):
    paginator = Paginator(blog, 3)  # Show 3 blogs per page
    page = request.GET.get('page')

    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    return blogs

def sidebar(request):
    blog = Blog.objects.all()
    # Annotate each blog with the count of comments
    blog_with_comment_count = blog.annotate(comment_count=Count('comment'))

    # side bar category count
    
    grouped_blogs = {}
    
    for blog_post in blog_with_comment_count :
        comment_count = blog_post.comment_count
        if comment_count not in grouped_blogs:
            grouped_blogs[comment_count] = []
        grouped_blogs[comment_count].append(blog_post)


    # Select the top posts from each group
    popular_posts = []
    for comment_count, posts in sorted(grouped_blogs.items(), reverse=True):
        popular_posts.extend(posts[:3])
    return popular_posts

def comment(request, blog):
    user = request.user
    if request.method == 'POST':
        comment = request.POST.get('comment')

        save_comment = Comment(user = user, content = comment, blog=blog)
        if user.is_authenticated:
            save_comment.save()
            messages.info(request, 'Thanks for making a comment')
            return redirect(reverse('blog_detail', args=[blog.id]))

        messages.info(request, 'You have to register first to comment')
        return redirect(reverse('blog_detail', args=[blog.id]))