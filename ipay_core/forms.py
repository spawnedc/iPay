from django import forms
from django.utils.translation import ugettext as _

from ipay_core.models import Payment
from ipay_core.constants import MONTH_CHOICES, DAY_CHOICES, DAYS

from django.forms.widgets import TextInput, DateInput, TimeInput

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


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

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.html5_required = True
        self.helper.add_input(Submit('submit', _('Submit')))

        super(BaseModelForm, self).__init__(*args, **kwargs)


class PaymentForm(BaseModelForm):
    repeat_month = forms.CharField(label=_('Month'), widget=forms.Select(choices=MONTH_CHOICES))
    repeat_weekday = forms.CharField(label=_('Weekday'), widget=forms.Select(choices=DAY_CHOICES))
    repeat_monthday = forms.CharField(label=_('Day'), widget=forms.Select(choices=DAYS))

    class Meta:
        model = Payment
        fields = ('title', 'amount', 'start_date', 'is_recurring', 'repeat_month', 'repeat_weekday', 'repeat_monthday')

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'e.g. Rent'
        self.fields['amount'].widget = NumberInput(attrs={'placeholder': 'e.g. 1234.56', 'step': '0.1', 'min': '0.1'})
        self.fields['start_date'].widget = DateInput()
