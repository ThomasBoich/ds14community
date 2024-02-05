from django import template
from posts.models import Category

register = template.Library()

@register.inclusion_tag('index/menu.html')
def display_menu():
    main_categories = Category.objects.filter(parent_category__isnull=True).prefetch_related('subcategories')
    return {'main_categories': main_categories}