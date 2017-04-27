from django.db import models

class Fish(models.Model):
    name = models.CharField(max_length=255, default='')

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        verbose_name = 'Fish'
        verbose_name_plural = 'Fishes'
        app_label = "api"


class Widget(models.Model):
    referrer_url = models.TextField(blank=True, null=True)
    whenhub_url = models.TextField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.referrer_url)

    class Meta:
        verbose_name = 'Widget'
        verbose_name_plural = 'Widgets'
        app_label = "api"