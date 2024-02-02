from django.contrib import admin
from .models import Post, Category
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_add', 'author', 'category']
    search_fields = ['title', 'description']
    readonly_fields = ('created_add',)



@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Post, PostAdmin)