from django.urls import path
from .views import show_blogs,create_blog,delete_blog,update_blog,register,custom_login,custom_logout,like_unlike_post,post_detail
from django.contrib.auth.decorators import login_required

urlpatterns = [
  path('', show_blogs, name='show_blogs'),
  path('blogs/', show_blogs, name='show_blogs'),
  path('blogs/create/', login_required(create_blog,login_url='/users/login/'), name='create_blog'),
  path('blogs/delete/<int:pk>/', login_required(delete_blog,login_url='/users/login/'), name='delete_blog'),
  path('blogs/update/<int:pk>/', login_required(update_blog,login_url='/users/login/'), name='update_blog'),
  path('blogs/like/<int:pk>/', like_unlike_post, name='like_unlike_post'),
  path('blogs/<int:pk>/', post_detail, name='post_detail'),

  path('users/register/', register, name='register'),
  path('users/login/', custom_login, name='custom_login'),
  path('users/logout/', custom_logout, name='logout'),

]
