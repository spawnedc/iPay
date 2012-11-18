from ipay_core.views import PublicBasicPageView

class Dashboard(PublicBasicPageView):

    template_name = 'dashboard.html'
    section_name = 'dashboard'

dashboard = Dashboard.as_view()