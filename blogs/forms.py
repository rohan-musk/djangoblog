from django import forms
from .models import BlogPost,Comment

#form for adding new blog post
class PostForm(forms.ModelForm):
  class Meta:
    model = BlogPost
    fields = ['title', 'content']

#form for adding new comment
class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['text','parent_comment']
