from django.contrib import admin
from django.db import models

# See http://pypi.python.org/pypi/croniter/
from croniter import croniter
from datetime import datetime

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

    title = models.CharField(max_length=200, null=False, blank=False, help_text='Title of this payment.')
    start_date = models.DateField(null=False, blank=False, help_text='Start date of this payment.')
    amount = models.DecimalField(max_digits=10, null=False, blank=False, decimal_places=2, help_text='Amount of this payment.')
    is_recurring = models.BooleanField(default=False, help_text='You can select this to set recurring options.')
    repeat_year = models.CharField(max_length=200, default='*')
    repeat_month = models.CharField(max_length=200, default='*')
    repeat_week = models.CharField(max_length=200, default='*')
    repeat_weekday = models.CharField(max_length=200, default='*')
    repeat_monthday = models.CharField(max_length=200, default='*')

    def __unicode__(self):
        return '%(title)s %(amount).2f, next payment on %(date)s' % ({
            'amount': self.amount,
            'title': self.title,
            'date': self.get_next_payment().strftime('%d %B %Y')
        })

    def get_cron_string(self):
        if not self.repeat_weekday == '*':
            return '0 12 * %s %s' % (self.repeat_month, self.repeat_weekday)
        else:
            return '0 12 %s %s *' % (self.repeat_monthday, self.repeat_month)

    def get_next_payment(self):
        today = datetime.now()
        croniter_obj = croniter(self.get_cron_string(), today)
        return croniter_obj.get_next(datetime)

admin.site.register(Payment)