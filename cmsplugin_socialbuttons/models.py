# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin


class Button(CMSPlugin):
    """Model for the ButtonPlugin."""

    icon_class = models.CharField(max_length=40, verbose_name=_(u'Icon class'))
    title = models.CharField(max_length=40, verbose_name=_(u'Title'))
    url = models.URLField(verbose_name=_(u'Link'))