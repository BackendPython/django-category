from django.db import models
from django.contrib.auth.models import AbstractUser

class Admin(AbstractUser):
    pass

class CardValues(models.Model):
    card_image = models.ImageField()
    category = models.ForeignKey("Category", blank=True, on_delete=models.CASCADE)
    card_title = models.CharField(max_length=150)
    
    def __str__(self):
        return self.card_title

class Category(models.Model):
    class Meta:
        verbose_name = 'My category'
        verbose_name_plural = 'My categorys'
    category_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category_name