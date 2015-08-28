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


class Area(BaseContentModel):

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Editable Area')
        verbose_name_plural = _('Editable Areas')


class SocialMedia(BaseContentOrderModel):
    link = models.URLField(verbose_name=_('link'))
    css_logo_class = models.CharField(
        max_length=25, verbose_name='Css logo class')
    css_container_class = models.CharField(
        max_length=25, verbose_name='Css container class')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Social Media')
        verbose_name_plural = _('Social Media')


class FeaturedVideo(BaseContentOrderModel):
    link = models.URLField(verbose_name=_('link'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Featured Video')
        verbose_name_plural = _('Featured Videos')
