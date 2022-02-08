from django.db import models


class MedDRAModelMixin(models.Model):
    """ Abstract model class for medDRA search field.
    """

    search_code = models.CharField(
        verbose_name='Search MedDRA dictionary',
        max_length=100,
        blank=True,
        null=True)

    class Meta:
        abstract = True
