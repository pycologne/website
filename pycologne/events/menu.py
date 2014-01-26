import datetime

from cms.menu_bases import CMSAttachMenu
from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from .models import Event

# config?
NUM_EVENTS_IN_MENU = 2

class EventsMenu(CMSAttachMenu):
    name = _("Events Menu")  # give the menu a name, this is required.

    def get_nodes(self, request):
        """
        This method is used to build a menu for the Events.
        It selects the (at most two) upcoming Events in the future.
        If no future Event can be found the most recent Event is selected.
        Finally a link to a list of all events is added to the menu.
        """
        nodes = []
        pos = 0
        now = datetime.datetime.utcnow()
        upcoming = Event.objects.filter(date__gt=now).order_by('date')
        if upcoming:
            upcoming = upcoming[:NUM_EVENTS_IN_MENU]
        else:
            upcoming = Event.objects.filter(date__lt=now).order_by('date')
            upcoming = upcoming[-1] if upcoming else []

        for evt in upcoming:
            # the menu tree consists of NavigationNode instances
            # Each NavigationNode takes a label as its first argument, a URL as
            # its second argument and a (for this tree) unique id as its third
            # argument.
            node = NavigationNode(
                evt.title,
                reverse('pycologne.events.details', args=(evt.pk,)),
                pos)
            nodes.append(node)
            pos += 1
        nodes.append(NavigationNode(
                _('All Events'),
                reverse('pycologne.events.all'),
                pos))
        return nodes

menu_pool.register_menu(EventsMenu) # register the menu.
