from django.core.urlresolvers import reverse

from ipay_core.views import PublicBasicPageView, PublicCreateView
from ipay_core.models import Payment
from ipay_core.forms import PaymentCreateForm

class Dashboard(PublicBasicPageView):

    template_name = 'dashboard.html'
    section_name = 'dashboard'

    def get_context_data(self):
        context = super(Dashboard, self).get_context_data()

        context['payments'] = Payment.objects.all().order_by('-start_date')

        return context

dashboard = Dashboard.as_view()


class CreatePayment(PublicCreateView):

    form_class = PaymentCreateForm

    template_name = 'create_payment.html'
    section_name = 'create_payment'

    success_url = '/'

create_payment = CreatePayment.as_view()