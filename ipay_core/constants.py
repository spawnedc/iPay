from django.utils.translation import ugettext as _

MONTH_CHOICES = [('*', _('Every month')),
                 ('1', _('January')),
                 ('2', _('February')),
                 ('3', _('March')),
                 ('4', _('April')),
                 ('5', _('May')),
                 ('6', _('June')),
                 ('7', _('July')),
                 ('8', _('August')),
                 ('9', _('September')),
                 ('10', _('October')),
                 ('11', _('November')),
                 ('12', _('December')),]

DAY_CHOICES = [('*', _('Every weekday')),
               ('1', _('Monday')),
               ('2', _('Tuesday')),
               ('3', _('Wednesday')),
               ('4', _('Thursday')),
               ('5', _('Friday')),
               ('6', _('Saturday')),
               ('7', _('Sunday')),]

DAYS = [('*', _('Every day'))] + [(day, day) for day in range(1,32)]