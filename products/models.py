from django.db import models
from django.conf import settings
import os

class TequilaType(models.Model):
    name = models.CharField(max_length=60)
    bimage = models.ImageField(
        upload_to='images/tequila/',
        default=os.path.join(settings.STATIC_ROOT,'generic_profile_image.png'),
    )
    maskimage = models.ImageField(
        upload_to='images/tequila/',
        default=os.path.join(settings.STATIC_ROOT,'generic_profile_image.png'),
    )

    def __unicode__(self):
        return self.name


class EventType(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name


class Template(models.Model):
    name = models.CharField(max_length=60)
    etype = models.ForeignKey('EventType', default=1, related_name='templates')
    timage = models.ImageField(
        upload_to='images/templates/',
        default=os.path.join(settings.STATIC_ROOT,'generic_profile_image.png'),
    )

    def __unicode__(self):
        return self.name


class BoxPresentation(models.Model):
    bottlesize = models.CharField(max_length=20)
    bottles = models.PositiveSmallIntegerField()
    maxlabels = models.PositiveSmallIntegerField()
    bottlerow = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return self.bottlesize