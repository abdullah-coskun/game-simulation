from django.db import models

# Create your models here.
import uuid


class Score(models.Model):
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=False)
    points = models.IntegerField(blank=False, null=False, db_index=True, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)