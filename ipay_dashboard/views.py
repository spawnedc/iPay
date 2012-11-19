from ipay_core.views import PublicBasicPageView
from ipay_core.models import Payment

class Dashboard(PublicBasicPageView):

    template_name = 'dashboard.html'
    section_name = 'dashboard'

    def get_context_data(self):
        context = super(Dashboard, self).get_context_data()

        context['payments'] = Payment.objects.all().order_by('-date')

        return context

dashboard = Dashboard.as_view()