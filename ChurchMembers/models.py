from django.db import models
from django.db.models. import
from django_localflavor_us.models import USStateField, PhoneNumberField
from django.urls import reverse
from django.utils import
from tagging.fields import TagField

class Family(models.Model):
    """Family model"""
    STATUS_CHOICES = (
        (0, 'Inactive'),
        (1, 'Active'),
    )
    name = models.CharField(max_length=256)
    slug = models.CharField(unique=True)
    photo = models.FileField(upload_to='family_photos', blank=True, help_text='An image that will be used as a thumbnail')
    status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=1)
    address = models.CharField(max_length=256, blank=True)
    address2 = models.CharField(max_length=256, blank=True)
    city = models.CharField(max_length=128, blank=True)
    state = USStateField(blank=True, default='AR')
    zip = models.CharField(_('zip'), blank=True, max_length=10)
    phone1 = PhoneNumberField(_('phone'), blank=True)
    phone2 = PhoneNumberField(_('other phone'), blank=True)
    email = models.CharField(max_length=256, blank=True)
    website = models.URLField(max_length=256, blank=True)
    notes = models.TextField(blank=True)
    tags = TagField()

    class Meta:
        db_table = 'membership_families'
        verbose_name_plural = 'families'

    def __unicode__(self):
        return '%s family' % self.name


    def get_absolute_url(self):
      return reverse('family_detail', None, { 'slug': self.slug })
