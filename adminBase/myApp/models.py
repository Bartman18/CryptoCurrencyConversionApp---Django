from django.db import models

# Create your models here.
class CryptoCurrency(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()

    def __str__(self):
        return self.name