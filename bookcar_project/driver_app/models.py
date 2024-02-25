from django.contrib.gis.db import models
import uuid
from phonenumber_field.modelfields import PhoneNumberField

class Driver(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.PointField()

    def __str__(self) -> str:
        return self.name


class Cab(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    driver_id = models.OneToOneField(Driver, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=20)
    type = models.CharField(max_length=20, blank = True)
    price_ratio = models.FloatField()

    def __str__(self) -> str:
        return self.title

