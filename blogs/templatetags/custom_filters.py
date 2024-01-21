from django import template
from ..models import Like

register = template.Library()

@register.filter(name='user_has_liked')
def user_has_liked(post, user):
    return Like.objects.filter(post=post, user=user).exists()
