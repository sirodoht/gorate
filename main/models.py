from django.db import models


class Rating(models.Model):
    title = models.CharField(max_length=300)
    value = models.PositiveIntegerField()
