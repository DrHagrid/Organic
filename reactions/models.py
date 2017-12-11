from django.db import models
from classes.models import OrganicClass


def transform(inp):
    res = ''
    for i in range(0, len(inp)):
        if inp[i].isdigit():
            if (i == 0) or (inp[i - 1].isspace()):
                res += inp[i]
            else:
                res += '<sub>' + inp[i] + '</sub>'
        else:
            res += inp[i]
    return res


class Reaction(models.Model):
    organic_class = models.ForeignKey(OrganicClass)
    name = models.CharField(max_length=128)
    materials = models.CharField(max_length=256)
    products = models.CharField(max_length=256)
    conditions = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='reactions', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    materials_trans = models.CharField(max_length=256, blank=True, null=True, default=None)
    products_trans = models.CharField(max_length=256, blank=True, null=True, default=None)

    def __str__(self):
        return "%s %s" % (self.organic_class.name, self.name.lower())

    class Meta:
        verbose_name = 'Реакция'
        verbose_name_plural = 'Реакции'

    def save(self, *args, **kwargs):
        self.materials_trans = transform(self.materials)
        self.products_trans = transform(self.products)

        super(Reaction, self).save(*args, **kwargs)


class ReceivingReaction(models.Model):
    organic_class = models.ForeignKey(OrganicClass)
    name = models.CharField(max_length=128)
    materials = models.CharField(max_length=256)
    products = models.CharField(max_length=256)
    conditions = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='reactions', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    materials_trans = models.CharField(max_length=256, blank=True, null=True, default=None)
    products_trans = models.CharField(max_length=256, blank=True, null=True, default=None)

    def __str__(self):
        return "%s | %s" % (self.organic_class.name, self.name.lower())

    class Meta:
        verbose_name = 'Реакция получения'
        verbose_name_plural = 'Реакции получения'

    def save(self, *args, **kwargs):
        self.materials_trans = transform(self.materials)
        self.products_trans = transform(self.products)

        super(ReceivingReaction, self).save(*args, **kwargs)
