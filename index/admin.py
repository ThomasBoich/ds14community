from django.contrib import admin

# Register your models here.
from .models import Baner


@admin.register(Baner)
class BanerAdmin(admin.ModelAdmin):
    list_display = ('text',)
    #pass