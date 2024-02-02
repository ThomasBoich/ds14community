from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('categories/<cat_id>/', list_categories, name='list_categories')
]