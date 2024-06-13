from django.db import models
import uuid

# Create your models here.


class Car(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    mileage = models.IntegerField()

    def __str__(self):
        return f"{self.name}<{self.uid}>"
