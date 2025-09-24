from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    CATEGORY_CHOICES = [
        ('bola', 'Bola'),
        ('baju', 'Baju'),
        ('celana', 'Celana'),
        ('gear', 'Gear'),
        ('alat', 'Alat'),
    ]
     

    name = models.CharField(max_length=500)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    product_views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    @property
    def is_product_hot(self):
        return self.product_views > 20
        
    def increment_views(self):
        self.product_views += 1
        self.save(update_fields=['product_views'])

# class Dosen(models.Model):
#     nama = models.CharField(max_length=50)
#     umur = models.IntegerField()
#     biodata = models.TextField()
