from django.db import models
from .validators import *
import uuid

# Create your models here.
class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shortDescription = models.CharField(max_length=200, validators=[short_desc_validator])
    price = models.DecimalField(validators=[price_validator], decimal_places=2, max_digits=60)

    def save(self, *args, **kwargs):
        # Invoking full_clean will run the validators for each field
        self.full_clean()
        return super().save(*args, **kwargs)

class Receipt(models.Model):
    # Create UUID as the primary key
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    retailer = models.CharField(max_length=100, validators=[retailer_validator])
    purchaseDate = models.DateField()

    # Set purchaseTime as textfield because django's timeField only stores time
    # in format HH:MM:ss. The validator will validate that the value has correct
    # time format
    purchaseTime = models.TimeField()
    total = models.DecimalField(validators=[price_validator], decimal_places=2, max_digits=60)
    items = models.ManyToManyField(Item)

    def save(self, *args, **kwargs):
        # Invoking full_clean will run the validators for each field
        self.full_clean()
        return super().save(*args, **kwargs)
