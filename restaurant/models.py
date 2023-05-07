from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Booking(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    guests = models.IntegerField()
    table = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.user.first_name}, {self.table}: {self.date}"

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f"{self.title} : {str(self.price)}"
