import datetime

from django.conf import settings
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.urls import reverse


class Contact(TimeStampedModel):
    name = models.CharField(max_length=30, null=True, blank=True)
    company = models.CharField(max_length=50, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    extension = models.CharField(max_length=5, null=True, blank=True)
    last_contact_date = models.DateField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
         """
         Returns the url to access a particular lease.
         """
         return reverse('sale-detail', args=[str(self.id)])

    class Meta:
        ordering = ["last_contact_date"]


class Business(TimeStampedModel):
    name = models.CharField(max_length=30, null=True, blank=True)
    web_site = models.URLField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)



class Note(TimeStampedModel):
    note = models.TextField()
