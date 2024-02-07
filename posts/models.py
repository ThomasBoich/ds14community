
from ckeditor.fields import RichTextField
from django.db import models
from users.models import CustomUser
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.CharField(max_length=255, verbose_name='Описание')
    text = CKEditor5Field(config_name='extends', verbose_name='Текст')
    created_add = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(CustomUser, related_name='like_user', blank=True, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Категория')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name='Описание')
    # subcategories = models.ManyToManyField('self', blank=True, symmetrical=False)
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subcategories', verbose_name='Подкатегории')
    image = models.ImageField(upload_to='Categories/Images/%Y/%m/%d/', blank=True, null=True, verbose_name='Значок')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'