from django.db import models
from django.contrib.auth.models import User


MEAL_TYPE = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main_dishes", "Main Dishes"),
    ("desserts", "Desserts")
)

STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)


class Item(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(max_length=200, choices=MEAL_TYPE)
    # CASCADE - If a user is deleted, all the meals created by this user will be deleted at the same time
    # PROTECT - If a user is deleted, all the meals created by this user remain
    # SET_NULL - If a user is deleted, the author part of all the meals created by this user will be set to null
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True) # auto_now_add - Record the timestamp
    date_updated = models.DateTimeField(auto_now=True)# auto_now - Record the time when the item is edited

    def __str__(self):
        return self.meal


