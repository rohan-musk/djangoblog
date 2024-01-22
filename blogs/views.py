from django.shortcuts import render,redirect,get_object_or_404
from .models import BlogPost,Like, Comment
from .forms import PostForm,CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#view to register user - not protected
def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('show_blogs')
  else:
    form = UserCreationForm()
  return render(request, 'users/register.html', {'form': form})

#view to login user - not protected
def custom_login(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect('show_blogs')
  else:
    form = AuthenticationForm()
  return render(request, 'users/login.html', {'form': form})

#view to logout user - not protected
def custom_logout(request):
  logout(request)
  return redirect('show_blogs')

#view to display all posts - not protected
def show_blogs(request):
  blogposts = BlogPost.objects.all()
  page = request.GET.get('page', 1)
    
  paginator = Paginator(blogposts, 6)  

  try:
    blogposts = paginator.page(page)
  except PageNotAnInteger:
    blogposts = paginator.page(1)
  except EmptyPage:
    blogposts = paginator.page(paginator.num_pages)
  return render(request, 'blogs/blogpost_list.html', {'blogposts': blogposts})

#view to write blogs - protected- needs login
@login_required
def create_blog(request):
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user  
      post.save()
      return redirect('show_blogs')
  else:
    form = PostForm()
  return render(request, 'blogs/create_blog.html', {'form': form})

#view to delete blogs - protected- needs login
@login_required
def delete_blog(request, pk):
  blogpost = get_object_or_404(BlogPost, pk=pk)
  if request.user == blogpost.author:
    if request.method == 'POST':
      blogpost.delete()
      return redirect('show_blogs')
    return render(request, 'blogs/delete_blog.html', {'blogpost': blogpost})
  else:
    return redirect('show_blogs')

#view to update blogs - protected- needs login
@login_required
def update_blog(request, pk):
  blogpost = get_object_or_404(BlogPost, pk=pk)
  if request.user == blogpost.author:
    if request.method == 'POST':
      form = PostForm(request.POST, instance=blogpost)
      if form.is_valid():
        form.save()
        return redirect('show_blogs')
    else:
      form = PostForm(instance=blogpost)
    return render(request, 'blogs/update_blog.html', {'form': form, 'blogpost': blogpost})
  else:
    return redirect('show_blogs')

#view to like and unlike blogs - protected- needs login
@login_required
def like_unlike_post(request, pk):
  post = get_object_or_404(BlogPost, pk=pk)

  like_instance = Like.objects.filter(post=post, user=request.user).first()

  if not like_instance :
    Like.objects.create(post=post, user=request.user)

  if like_instance:
    like_instance.delete()

  return redirect('show_blogs')

#view to write comments on blogs - protected- needs login
def post_detail(request, pk):
  post = get_object_or_404(BlogPost, pk=pk)
  comments = Comment.objects.filter(post=post, parent_comment__isnull=True)
  
  if request.method == 'POST':
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
      comment = comment_form.save(commit=False)
      comment.post = post
      comment.author = request.user
      comment.save()
      return redirect('post_detail', pk=pk)
  else:
      comment_form = CommentForm()

  return render(request, 'blogs/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})