from django.db import models
import uuid
from phonenumber_field.modelfields import PhoneNumberField

class Customer(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
