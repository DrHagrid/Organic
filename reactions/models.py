from django.db import models
from classes.models import OrganicClass


class Reaction(models.Model):
    organic_class = models.ForeignKey(OrganicClass)
    name = models.CharField(max_length=64)
    materials = models.CharField(max_length=128)
    products = models.CharField(max_length=128)
    conditions = models.CharField(max_length=128)

    def __str__(self):
        return "%s %s" % (self.organic_class.name, self.name.lower())

    class Meta:
        verbose_name = 'Реакция'
        verbose_name_plural = 'Реакции'


class ReceivingReaction(models.Model):
    organic_class = models.ForeignKey(OrganicClass)
    name = models.CharField(max_length=64)
    materials = models.CharField(max_length=128)
    products = models.CharField(max_length=128)
    conditions = models.CharField(max_length=128)

    def __str__(self):
        return "%s %s" % (self.organic_class.name, self.name.lower())

    class Meta:
        verbose_name = 'Реакция получения'
        verbose_name_plural = 'Реакции получения'
