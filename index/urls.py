from django.urls import path
from .views import *
from posts.views import create_post, create_category

urlpatterns = [
    path('login/', AppLoginView.as_view(), name='login'),
    path('', index, name='index'),
    path('categories/<cat_id>/', list_categories, name='list_categories'),
    path('categories/posts/<cat_id>/', sub_list_categories, name='sub_list_categories'),
    path('categories/post/<post_id>/', post, name='post'),
    path('post/new/', create_post, name='post_new'),
    path('category/new/', create_category, name='category_new'),
    path('profile/', profile, name='profile')
]