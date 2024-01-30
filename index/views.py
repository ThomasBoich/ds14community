from django.shortcuts import render
from posts.models import *


# Create your views here.
def index(request):
    categories = Category.objects.filter(subcategories__isnull=False).distinct()
    context = {
        'categories': categories,
    }
    
    return render(request, 'index/index.html', context)