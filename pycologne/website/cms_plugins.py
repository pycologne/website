# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from pycologne.website import models

class JumbotronPlugin(CMSPluginBase):
    """Creates a Bootstrap Jumbotron."""

    render_template = 'website/jumbotron.html'
    name = _(u'Jumbotron')
    model = models.Jumbotron

plugin_pool.register_plugin(JumbotronPlugin)