from django.db import models

# Create your models here.

class Baner(models.Model):
    text = models.CharField(max_length=255)
    image = models.ImageField(upload_to='baners/%Y/%m/%d/')

    class Meta:
        verbose_name = 'Банер'
        verbose_name_plural = 'Банеры'

    def __str__(self):
        return self.text