from django.db import models
from django.utils.translation import ugettext as _


def model_directory_path(instance, filename):
    return instance.__class__.__name__+'/'+filename

class BaseCatalogModel(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('Name'))

    class Meta:
        abstract = True


class BaseContentModel(models.Model):
    title = models.CharField(max_length=150, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))

    class Meta:
        abstract = True


class BaseContentOrderModel(BaseContentModel):
    order = models.PositiveIntegerField(unique=True, verbose_name='Order')

    class Meta:
        abstract = True


class BaseGallerieImageModel(BaseContentModel):
    image = models.ImageField(
        upload_to=model_directory_path, verbose_name=_('Image'))

    class Meta:
        abstract = True


class BaseGallerieNavImageModel(BaseGallerieImageModel):
    target = models.BooleanField(default=False, help_text=_('Open in new tab'))
    link = models.URLField(blank=True, null=True, verbose_name=_('Link'))

    class Meta:
        abstract = True


