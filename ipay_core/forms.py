from django import forms
from django.utils.translation import ugettext as _

from ipay_core.models import Payment
from ipay_core.constants import MONTH_CHOICES, DAY_CHOICES, DAYS

from django.forms.widgets import TextInput, DateInput, DateTimeInput, TimeInput

class BaseInput(forms.Widget):
    class Meta:
        abstract = True

class EmailInput(TextInput):
    input_type = 'email'

class NumberInput(TextInput):
    input_type = 'number'

class DateInput(DateInput):
    input_type = 'date'

class TimeInput(TimeInput):
    input_type = 'time'

class BaseModelForm(forms.ModelForm):
    class Meta:
        abstract = True

    def set_required_fields(self):
        """ Sets the 'required' attribute to 'true' on necessary form fields """

        for field in self.fields:
            if self.fields[field].required:
                self.fields[field].widget.attrs['required'] = 'true'

    def as_bootstrap(self, style='horizontal'):
        """ Outputs the form using bootstrap markup """

        # TODO: Implement other types of forms as well,
        # e.g. inline, search and default
        # See: http://twitter.github.com/bootstrap/base-css.html#forms

        markup = ''

        for key in self.fields:
            field = self.fields.get(key)
            field_id = 'id_' + key
            widget = field.widget.render(key, field.initial, { 'id': field.widget.id_for_label(field_id) })

            markup += '<div class="control-group">\n\
                           <label class="control-label" for="%s">%s</label>\n\
                           <div class="controls">\n\
                               %s\n\
                           </div>\n\
                       </div>\n' % (field.widget.id_for_label(field_id), _(field.label), widget)

        return markup

class PaymentCreateForm(BaseModelForm):
    repeat_month = forms.CharField(label='Month', widget=forms.Select(choices=MONTH_CHOICES))
    repeat_weekday = forms.CharField(label='Weekday', widget=forms.Select(choices=DAY_CHOICES))
    repeat_monthday = forms.CharField(label='Day', widget=forms.Select(choices=DAYS))

    class Meta:
        model = Payment
        fields = ('title', 'amount', 'start_date', 'is_recurring', 'repeat_month', 'repeat_weekday', 'repeat_monthday')

    def __init__(self, *args, **kwargs):
        super(PaymentCreateForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'e.g. Rent'
        self.fields['amount'].widget = NumberInput(attrs={'placeholder': 'e.g. 1234.56', 'step': '0.1', 'min': '0.1'})
        self.fields['start_date'].widget = DateInput()

        self.set_required_fields()