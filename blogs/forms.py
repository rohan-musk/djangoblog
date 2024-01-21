from django import forms
from .models import BlogPost,Comment

class PostForm(forms.ModelForm):
  class Meta:
    model = BlogPost
    fields = ['title', 'content']

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['text','parent_comment']
