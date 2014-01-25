# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cmsplugin_socialbuttons import models


class ButtonListPlugin(CMSPluginBase):

    render_template = 'cmsplugin_socialbuttons/button_list.html'
    name = _(u'Button list')
    allow_children = True
    child_classes = ['ButtonPlugin',]


class ButtonPlugin(CMSPluginBase):

    model = models.Button
    render_template = 'cmsplugin_socialbuttons/button.html'
    name = _(u'Button')
    require_parent = True
    parent_classes = ['ButtonListPlugin',]


plugin_pool.register_plugin(ButtonListPlugin)
plugin_pool.register_plugin(ButtonPlugin)
