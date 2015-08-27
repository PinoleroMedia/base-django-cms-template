from django.db import models
from django.utils.translation import ugettext as _
from core.models import *


class BaseCatalogi18nModel(BaseCatalogModel):
    name_es = models.CharField(max_length=150, verbose_name=_('Name'),
                               blank=True,
                               null=True)

    def get_name(self, language):
        if language == 'es' and self.title_es is not None and self.title_es:
            return self.title_es
        return self.title

    class Meta:
        abstract = True


class BaseContenti18nModel(BaseContentModel):
    title_es = models.CharField(max_length=160,
                                blank=True,
                                null=True)
    description_es = models.TextField(blank=True,
                                      null=True)

    def get_title(self, language):
        if language == 'es' and self.title_es is not None and self.title_es:
            return self.title_es
        return self.title

     def get_description(self, language):
        if language == 'es' and self.description_es is not None and self.description_es:
            return self.description_es
        return self.title

    class Meta:
        abstract = True

class BaseContentOrderi18nModel(BaseContenti18nModel, BaseContentOrderModel):
    
    class Meta:
        abstract = True

class BaseGallerieiImagei18nModel(BaseContenti18nModel, BaseGallerieImageModel):

    class Meta:
        abstract = True

class BaseGallerieNavImagei18nModel(BaseGallerieiImagei18nModel, BaseGallerieNavImageModel):
    target = models.BooleanField(default=False, help_text=_('Open in new tab'))
    link = models.URLField(blank=True, null=True, verbose_name=_('Link'))

    class Meta:
        abstract = True
