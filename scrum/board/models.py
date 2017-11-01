from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Sprint(models.Model):
    """ Development iteration period. """
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    end = models.DateField(unique=True)

    def __str__(self):
        return self.name or _('Sprint ending %s') % self.end

class Task(models.Model):
    """ Unit of work to be done for the sprint """
    STATUS_ORDER_RECEIVED = 1
    STATUS_CORRUGATION = 2
    STATUS_PASTING = 3
    STATUS_CREASING = 4
    STATUS_SLOTTING = 5
    STATUS_STITCHING = 6
    STATUS_BUNDLING = 7
    STATUS_DISPATCHED = 8
    STATUS_COMPLETE = 9

    STATUS_CHOICES = (
        (STATUS_ORDER_RECEIVED, _('Not Started')),
        (STATUS_CORRUGATION, _('Corrugation')),
        (STATUS_PASTING, _('Pasting')),
        (STATUS_CREASING, _('Creasing')),
        (STATUS_SLOTTING, _('Slotting')),
        (STATUS_STITCHING, _('Stitching')),
        (STATUS_BUNDLING, _('Bundling')),
        (STATUS_DISPATCHED, _('Dispatched')),
        (STATUS_COMPLETE, _('Complete')),
    )

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    sprint = models.ForeignKey(Sprint, blank=True, null=True)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=STATUS_ORDER_RECEIVED)
    order = models.SmallIntegerField(default=0)
    assigned = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    started = models.DateField(blank=True, null=True)
    due = models.DateField(blank=True, null=True)
    completed = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name