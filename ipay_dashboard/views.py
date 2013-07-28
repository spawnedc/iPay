from ipay_core.views import PublicBasicPageView, PublicCreateView, PublicUpdateView
from ipay_core.models import Payment
from ipay_core.forms import PaymentForm


class Dashboard(PublicBasicPageView):

    template_name = 'dashboard.html'
    section_name = 'dashboard'

    def get_context_data(self):
        context = super(Dashboard, self).get_context_data()

        context['payments'] = Payment.objects.all().order_by('-start_date')

        return context

dashboard = Dashboard.as_view()


class CreatePayment(PublicCreateView):

    form_class = PaymentForm

    template_name = 'create_payment.html'
    section_name = 'create_payment'

    success_url = '/'

create_payment = CreatePayment.as_view()


class EditPayment(PublicUpdateView):

    model = Payment
    form_class = PaymentForm
    template_name = 'create_payment.html'
    section_name = 'create_payment'
    success_url = '/'

edit_payment = EditPayment.as_view()
