from django.views.generic.base import View, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from ipay.settings import APP_TITLE

class PublicBaseView(View):
    """ A base class for all views """

    class Meta:
        abstract = True

    def get_context_data(self, *args, **kwargs):
        context = super(PublicBaseView, self).get_context_data(*args, **kwargs)

        context['section'] = self.section_name or ''
        context['APP_TITLE'] = APP_TITLE

        return context

class PublicBasicPageView(PublicBaseView, TemplateView):
    """ Basic page view """
    pass

class PublicDetailView(PublicBaseView, DetailView):
    """ Basic detail page view """
    pass

class PublicListView(PublicBaseView, ListView):
    """ Basic list view """
    pass

class PublicCreateView(PublicBaseView, CreateView):
    """ Basic create view """
    pass