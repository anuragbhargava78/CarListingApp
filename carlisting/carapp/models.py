from django.db import models

class Car(models.Model):
    CONDITION_CHOICES = (
        ('Poor', 'Poor'),
        ('Fair', 'Fair'),
        ('Good', 'Good'),
        ('Excellent', 'Excellent'),
    )
    
    seller_name = models.CharField(max_length=100)
    seller_mobile = models.CharField(max_length=15)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.DateField()
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    asking_price = models.DecimalField(max_digits=8, decimal_places=2)

    is_sold = models.BooleanField(default=False)

