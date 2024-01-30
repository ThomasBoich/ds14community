from django.contrib import admin
from .models import Post, Category

# Register your models here.


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('title',)
    
@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('name',)