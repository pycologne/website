# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin


EVENT_KIND_CHOICES = (
    (1, _('regular')),
    (2, _('exhibition')),
    (3, _('conference')),
)

PARTICIPATION_CHOICES = (
    (0, _(u'Decline')),
    (1, _(u'Attend')),
    (2, _(u'Maybe')),
)

class Location(models.Model):
    """Location represents a physical location (for an event).
    It has a title, address and an (optional) link
    to an external website.
    """
    title = models.CharField(_("Title"), max_length=255)
    slug = models.SlugField(_("slug"))
    postal = models.CharField(_("postal"), max_length=20, blank=True, null=True)
    street = models.CharField(_("street"), max_length=255, blank=True, null=True)
    city = models.CharField(_("city"), max_length=255, blank=True, null=True)
##    country = models.CharField(_("country"), max_length=2)
    link = models.URLField(_("Link"), blank=True, null=True)

    objects = models.Manager()

    def __unicode__(self):
        return self.title

    class Meta(object):
        verbose_name = _("location")
        verbose_name_plural = _("locations")
        ordering = ['title']


class Event(models.Model):
    """Event represents a scheduled event of a particular kind.
    It has a title, location, start and end date, as well
    as an (optional) link to an external website.
    """
    title = models.CharField(_("Title"), max_length=255)
    slug = models.SlugField(_("slug"))
    kind = models.IntegerField(_("kind"), choices=EVENT_KIND_CHOICES)
    date = models.DateTimeField(_("Date"))
    end_date = models.DateTimeField(_("End date"), blank=True, null=True)
    location = models.ForeignKey(Location, verbose_name=_("location"))
    link = models.URLField(_("Link"), blank=True, null=True)

    objects = models.Manager()

#    def __unicode__(self):
#        return self.title

    def __unicode__(self):
        return u"{0}, {1} ({2})".format(
            self.title,
            self.date.strftime('%d.%m.%Y'),
            self.get_kind_display())

    class Meta(object):
        verbose_name = _('event')
        verbose_name_plural = _('events')
        ordering = ['date']


class EventPlugin(CMSPlugin):
    """
    Plugin for Django CMS to show a particular event on a page.
    Shows details about the event and doesn't allow interaction.
    """
    event = models.ForeignKey('events.Event', related_name='plugins')

    def __unicode__(self):
        return self.event.title


class Participant(models.Model):
    """Participants for an event."""
    event = models.ForeignKey(Event, verbose_name=_(u'Event'))
    answer = models.IntegerField(_(u'Answer'), choices=PARTICIPATION_CHOICES)
    registered_participant = models.ForeignKey(User,
        verbose_name=_(u'Registered user'), blank=True, null=True)
    unregistered_user = models.CharField(_(u'Unregistered user'),
        max_length=100, blank=True, null=True)
