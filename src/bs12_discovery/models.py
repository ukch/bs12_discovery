from urlparse import urljoin

from django.db import models


class Account(models.Model):

    name = models.CharField(max_length=255, primary_key=True, unique=True)

    def __unicode__(self):
        return unicode(self.name)


class Service(models.Model):

    account = models.ForeignKey(Account, related_name="services")
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    service_path = models.FilePathField(max_length=255)

    class Meta:
        unique_together = ("account", "name")

    def __unicode__(self):
        return unicode(self.name)


class Server(models.Model):

    account = models.ForeignKey(Account, related_name="servers")
    description = models.CharField(max_length=255)
    services = models.ManyToManyField(Service, through="API",
                                      related_name="available_servers")
    base_url = models.URLField(max_length=255)

    def __unicode__(self):
        if self.description:
            return self.description
        return u"Unnamed server (%s)" % self.base_url


class API(models.Model):

    account = models.ForeignKey(Account, related_name="+")
    service = models.ForeignKey(Service, related_name="+")
    server = models.ForeignKey(Server, related_name="+")

    @property
    def url(self):
        return urljoin(self.server.base_url, self.service.service_path)

    def __unicode__(self):
        return unicode(self.name)
