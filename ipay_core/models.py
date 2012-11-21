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
    start_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_recurring = models.BooleanField(default=False)
    repeat_year = models.CharField(max_length=200, default='*')
    repeat_month = models.CharField(max_length=200, default='*')
    repeat_week = models.CharField(max_length=200, default='*')
    repeat_weekday = models.CharField(max_length=200, default='*')
    repeat_monthday = models.CharField(max_length=200, default='*')

    def __unicode__(self):
        return '%(title)s %(amount).2f, due on %(date)s' % ({'amount': self.amount, 'title': self.title, 'date': self.start_date})

admin.site.register(Payment)