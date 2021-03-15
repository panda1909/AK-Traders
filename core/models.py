from django.db import models
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