from django.db import models
import uuid 

class Vehicle(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, 
         editable = False)
    title = models.CharField(max_length=20)
    price = models.IntegerField(default=41000)
    image_path = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title