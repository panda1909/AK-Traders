from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Messages(models.Model):
    Name = models.CharField(max_length=128)
    Email = models.EmailField()
    Phone = PhoneNumberField()
    Message = models.TextField(max_length=5000)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "1 - Customer Query"
        verbose_name_plural = "1 - Customer Queries"

class Products(models.Model):
    Name = models.CharField(max_length=128)
    Description = models.TextField(max_length=1200)
    Image = models.FileField(upload_to='static/prods/')

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse( "detail-product" ,kwargs={"pk": self.pk})
    
    class Meta:
        verbose_name = "2 - Product"
        verbose_name_plural = "2 - Products"


class Quote(models.Model):
    Name = models.CharField(max_length=128)
    Email = models.EmailField()
    Phone = PhoneNumberField()
    Product = models.CharField(max_length=128)
    Quantity = models.PositiveIntegerField()
    Description = models.TextField(max_length=5000)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "3 - Quote"
        verbose_name_plural = "3 - Quotes"