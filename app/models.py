from django.db import models

# Create your models here.
class Coffee(models.Model):
    name = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.name


class Transaction(models.Model):
    time = models.DateTimeField()
    item = models.ForeignKey(Coffee, on_delete=models.CASCADE)
    pre_tax = models.FloatField()
    tax = models.FloatField()
