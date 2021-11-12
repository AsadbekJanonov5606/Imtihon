from django.db import models


class Countries(models.Model):
    name = models.CharField(max_length=200, null=True)
    provinces = models.CharField(max_length=200, null=True)

