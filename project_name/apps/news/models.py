from django.db import models
from django.utils.translation import ugettext as _
from core.models import *


class New(BaseContentModel):
    date = models.DateTimeField(verbose_name=_('Date'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('New')
        verbose_name_plural = _('News')
        ordering = ('-date', )
