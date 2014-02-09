from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from .menu import EventsMenu

class EventsApp(CMSApp):
    name = _("events-app")
    urls = ["pycologne.events.urls"]
    menus = [EventsMenu] # attach a CMSAttachMenu to this apphook.

# register CMS App
apphook_pool.register(EventsApp)