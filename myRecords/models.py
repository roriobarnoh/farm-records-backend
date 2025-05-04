from django.db import models

# Create your models here.
class ChickenRecord(models.Model):
    date = models.DateField()
    hens = models.PositiveIntegerField()
    eggs = models.PositiveIntegerField()
    feed = models.IntegerField(help_text="In kilograms")
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date} - Hens: {self.hens}, Eggs : {self.eggs}"


class CowRecord(models.Model):
    date = models.DateField()
    cows = models.PositiveIntegerField()
    milk = models.IntegerField(help_text="In liters")
    feed = models.IntegerField(help_text="In kilograms")
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date} - Cows: {self.cows}, Milk : {self.milk}"


class HorticultureRecord(models.Model):
    CROP_TYPES = [
        ('Fruit', 'Fruit'),
        ('Vegetable', 'Vegetable'),
        ('Herb', 'Herb'),
        ('Flower', 'Flower'),
        ('Other', 'Other'),
    ]

    crop_name = models.CharField(max_length=100)
    crop_type = models.CharField(max_length=20, choices=CROP_TYPES)
    planting_date = models.DateField()
    harvest_date = models.DateField(null=True, blank=True)
    quantity_harvested = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    unit = models.CharField(max_length=20, default='kg')  # e.g. kg, tons, bunches
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.crop_name} ({self.crop_type})"

