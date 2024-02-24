from django.db import models

class Vehicle(models.Model):
    title = models.CharField(max_length=20)
    price = models.IntegerField(default=41000)
    image_path = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title
