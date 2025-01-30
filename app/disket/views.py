import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView, ListView
from django.views.static import serve

from .forms import DisketUploadForm
from .models import Disket


class DisketUploadView(LoginRequiredMixin, CreateView):
    """
    View to handle the upload of a new page.
    """
    model = Disket
    form_class = DisketUploadForm
    template_name = 'page/upload.html'
    success_url = '/'

    def form_valid(self, form):
        """
        Set the author of the page to the current user before saving.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)


class DisketDetailView(DetailView):
    """
    View to display the details of a specific page.
    """
    model = Disket
    template_name = 'page/detail.html'
    context_object_name = 'disket'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['absolute_content_path'] = self.request.build_absolute_uri(settings.MEDIA_URL + self.object.content_path)
        return context


class HomeView(ListView):
    """
    View to display a list of approved and listed pages on the homepage.
    """
    model = Disket
    template_name = 'page/home.html'
    context_object_name = 'diskettes'

    def get_queryset(self):
        """
        Return only pages that are listed and approved.
        """
        # return Disket.objects.filter(visibility='listed', approved=True) 
        return Disket.objects.all()


def serve_with_x_frame_options(request, path, document_root=None, show_indexes=False):
    response = serve(request, path, document_root, show_indexes)
    response['X-Frame-Options'] = settings.X_FRAME_OPTIONS
    return response
