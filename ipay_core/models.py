from django.contrib import admin
from django.db import models

class Person(models.Model):

    class Meta:
        abstract = True

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()

    thumbnail_image = models.CharField(max_length=200, null=True, default='meh')

    def __unicode__(self):
        return self.name

    @property
    def name(self):
        return "%s %s" % (self.first_name, self.last_name)


class Payment(models.Model):

    title = models.CharField(max_length=200)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return '%(title)s %(amount).2f, due on %(date)s' % ({'amount': self.amount, 'title': self.title, 'date': self.date})

admin.site.register(Payment)