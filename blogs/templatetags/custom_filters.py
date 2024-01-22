from django import template
from ..models import Like

register = template.Library()

#filer logic to check if a post has been liked by a user or not
@register.filter(name='user_has_liked')
def user_has_liked(post, user):
    return Like.objects.filter(post=post, user=user).exists()
