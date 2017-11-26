from django.db import models


class OrganicClass(models.Model):
    name = models.CharField(max_length=64)
    formula = models.CharField(max_length=16)
    properties = models.TextField()

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'
