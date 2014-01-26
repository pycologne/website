"""cms_plugins.py

Django CMS Plugin registration.
"""
import datetime

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import EventPlugin as EventPluginModel
from .models import Event
from django.utils.translation import ugettext as _

class EventPlugin(CMSPluginBase):
    """
    Plugin for Django CMS to show a selected event on a page.
    """
    model = EventPluginModel  # Model where data about this plugin is saved
    name = _("Event Plugin")  # Name of the plugin
    render_template = "events/event_plugin.html"  # template to render the plugin with

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context


class VotingPlugin(CMSPluginBase):
    """
    Plugin for Django CMS to show the next upcoming event on a page (if any).
    Shows details about the event and allows to vote about participation.
    """
    render_template = 'events/voting_plugin.html'
    name = _(u'Participant Voting Plugin')

    def render(self, context, instance, placeholder):
        now = datetime.datetime.utcnow()
        upcoming = Event.objects.filter(date__gt=now).order_by('date')
        if upcoming:
            upcoming = upcoming[0]
        context.update({'upcoming':upcoming})
        return context

# register the plugins:
plugin_pool.register_plugin(EventPlugin)
plugin_pool.register_plugin(VotingPlugin)
