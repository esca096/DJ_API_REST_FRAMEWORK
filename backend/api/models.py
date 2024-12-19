from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse("api:product_api_view_detail", kwargs={"pk": self.pk})
    
    
    def get_price_in_euros(self):
        return f'{self.price} €'
    
    def get_description(self):
        return f'{self.name} - {self.price} €'
      
    def __str__(self):
        return self.name