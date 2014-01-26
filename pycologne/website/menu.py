from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

class UserMenu(Menu):
    
    def get_nodes(self, request):
        """Extends the website menu with some user menu items.
        """
        return [
            NavigationNode(_("User"), '/' , 100),  # User Menu (right hand side)
# TODO            NavigationNode(_("Profile"), reverse(profile), 1, 100, attr={'visible_for_anonymous': False}),
            NavigationNode(_("Profile"), '/', 1, 100, attr={'visible_for_anonymous': False}),
            NavigationNode(_("Log in"), '/login', 3, 100, attr={'visible_for_authenticated': False}),
# TODO: registration form ?!
            NavigationNode(_("Sign up"), '/user/register', 4, 100, attr={'visible_for_authenticated': False}),
            NavigationNode(_("Log out"), '/logout', 2, 100, attr={'visible_for_anonymous': False}),
        ]

menu_pool.register_menu(UserMenu)
