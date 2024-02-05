from django.urls import path
from .views import *

urlpatterns = [
    path('login/', AppLoginView.as_view(), name='login'),
    path('', index, name='index'),
    path('categories/<cat_id>/', list_categories, name='list_categories'),
    path('categories/posts/<cat_id>/', sub_list_categories, name='sub_list_categories'),
    path('categories/post/<post_id>/', post, name='post')
]