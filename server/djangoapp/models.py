import sys
try:
    from django.db import models
except Exception:
    print("There was an error loading django modules. Do you have django installed?")
    sys.exit()

from django.utils.timezone import now
from django.conf import settings
import uuid


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=60)


    def __str__(self):
        return self.description

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    make = models.ManyToManyField(CarMake)
    dealerId = models.IntegerField()
    year = models.IntegerField()
    CAR_CHOICES = [
        ("SUV", "SUV"),
        ("SEDAN", "SEDAN"),
        ("WAGON", "WAGON"),
    ]
    carType = models.CharField(max_length=10, choices=CAR_CHOICES)

    def __str__(self):
        return f"{self.year} {self.carType}"

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
