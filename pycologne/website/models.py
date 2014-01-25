# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from djangocms_text_ckeditor.fields import HTMLField

from cms.models.fields import PageField
from cms.models.pluginmodel import CMSPlugin


class Jumbotron(CMSPlugin):
	"""Model for the JumbotronPlugin."""

	title = models.CharField(max_length=120, verbose_name=_(u'Title'))
	content = HTMLField(verbose_name=_(u'Text'))
	button_title = models.CharField(max_length=50,
									verbose_name=_(u'Button title'),
									null=True, blank=True)
	button_link = PageField(verbose_name=_(u'Button link'),
							null=True, blank=True)