from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.

class MyUser(User):
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    display_name = models.CharField(max_length=300, blank=True, null=True, unique=True)
    points = models.IntegerField(blank=False, null=False, db_index=True, default=0)
    country = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        indexes = (
            models.Index(fields=['-points']),
        )

    def __str__(self):
        return self.display_name
