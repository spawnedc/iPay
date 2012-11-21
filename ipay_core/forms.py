from django.forms import ModelForm
from ipay_core.models import Payment

class BaseModelForm(ModelForm):
    class Meta:
        abstract = True

    def as_bootstrap(self, style='horizontal'):
        """ Outputs the form using bootstrap markup """

        # TODO: Implement other types of forms as well,
        # e.g. inline, search and default
        # See: http://twitter.github.com/bootstrap/base-css.html#forms

        markup = ''

        print self.fields.get('title').widget.render('title', '')

        for key in self.fields:
            field = self.fields.get(key)
            widget = field.widget.render(key, field.initial, { 'id': field.widget.id_for_label })

            markup += '<div class="control-group">\
                <label class="control-label" for="%s">%s</label>\
                <div class="controls">\
                    %s\
                </div>\
            </div>' % (field.widget.id_for_label, field.label, widget)

        return markup

class PaymentCreateForm(BaseModelForm):
    class Meta:
        model = Payment