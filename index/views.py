from django.shortcuts import render
from posts.models import *
from django.shortcuts import render, get_object_or_404
from index.models import Baner

# Create your views here.
def index(request):
    categories = Category.objects.filter(subcategories__isnull=False).distinct()
    context = {
        'categories': categories,
        'baners': Baner.objects.all()
    }
    
    return render(request, 'index/index.html', context)


def list_categories(request, cat_id):

    # Получаем родительскую категорию
    parent_category = get_object_or_404(Category, id=cat_id)

    # Получаем подкатегории родительской категории
    subcategories = parent_category.subcategories.all()


    context = {
        'parent_category': parent_category,
        'subcategories': subcategories,
    }
    
    return render(request, 'index/list_categories.html', context)