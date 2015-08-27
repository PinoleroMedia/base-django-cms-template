from django.db import models
from django.utils.translation import ugettext as _
from core.models import *


class Section(BaseCatalogModel, BaseContentModel):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')
        ordering = ('id', )


class SectionImage(BaseGallerieNavImageModel):
    section = models.ForeignKey(Section, verbose_name=_('carousel'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Carousel')
