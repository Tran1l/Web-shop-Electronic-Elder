from django.db import models

# Create your models here.
class ProductCatagory(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=1)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="media")
    category = models.ForeignKey(to=ProductCatagory, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Продукт: {self.name} | Категория: {self.category.name}"
