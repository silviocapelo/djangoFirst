from django.db import models


# Create your models here.


class Cliente(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
