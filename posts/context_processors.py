from .models import Category

def categories(request):
    categories_as = Category.objects.filter(parent_category__isnull=True).prefetch_related('subcategories')
    return {'categories_as': categories_as}