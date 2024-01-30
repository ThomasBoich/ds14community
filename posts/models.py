from django.db import models
from users.models import CustomUser
# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    text = models.TextField()
    created_add = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(CustomUser, related_name='like_user')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        

class Category(models.Model):
    name = models.CharField(max_length=255)
    subcategories = models.ManyToManyField('self', blank=True, symmetrical=False)
    image = models.ImageField(upload_to='Categories/Images/%Y/%m/%d/', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'