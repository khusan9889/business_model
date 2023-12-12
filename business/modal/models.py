from django.db import models


class Modal(models.Model):
    name = models.CharField(max_length=100)

