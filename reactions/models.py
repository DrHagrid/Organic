from django.db import models
from classes.models import OrganicClass


class Reaction(models.Model):
    organic_class = models.ForeignKey(OrganicClass)
    name = models.CharField(max_length=128)
    materials = models.CharField(max_length=256)
    products = models.CharField(max_length=256)
    conditions = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='reactions', blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.organic_class.name, self.name.lower())

    class Meta:
        verbose_name = 'Реакция'
        verbose_name_plural = 'Реакции'


class ReceivingReaction(models.Model):
    organic_class = models.ForeignKey(OrganicClass)
    name = models.CharField(max_length=128)
    materials = models.CharField(max_length=256)
    products = models.CharField(max_length=256)
    conditions = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='reactions', blank=True, null=True)

    def __str__(self):
        return "%s | %s" % (self.organic_class.name, self.name.lower())

    class Meta:
        verbose_name = 'Реакция получения'
        verbose_name_plural = 'Реакции получения'
