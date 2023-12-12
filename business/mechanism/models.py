from django.db import models
from modal.models import Modal

class Mechanism(models.Model):
    name = models.CharField(max_length=1000, null=True, blank=True)
    model_id = models.ForeignKey(Modal, on_delete=models.CASCADE, null=True, blank=True)