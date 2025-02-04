import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.static import serve

from .forms import DisketUploadForm, DisketEditForm
from .models import Disket


class UploadView(LoginRequiredMixin, CreateView):
    """
    View to handle the upload of a new disket.
    """
    model = Disket
    form_class = DisketUploadForm
    template_name = 'disket/upload.html'
    success_url = '/'

    def form_valid(self, form):
        """
        Set the author of the disket to the current user before saving.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)


class DisketUpdateView(LoginRequiredMixin, UpdateView):
    """
    View to handle the editing of a disket.
    """
    model = Disket
    form_class = DisketEditForm
    template_name = 'disket/upload.html'
    success_url = '/'

    def get_object(self):
        return get_object_or_404(Disket, slug=self.kwargs['slug'])

class DisketDetailView(DetailView):
    """
    View to display the details of a specific disket.
    """
    model = Disket
    template_name = 'disket/detail.html'
    context_object_name = 'disket'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['absolute_content_path'] = self.request.build_absolute_uri(settings.MEDIA_URL + self.object.content_path)
        return context


class HomeView(ListView):
    """
    View to display a list of approved and listed diskets on the homedisket.
    """
    model = Disket
    template_name = 'disket/list.html'
    context_object_name = 'diskettes'

    def get_queryset(self):
        """
        Return only diskets that are listed and approved.
        """
        # return Disket.objects.filter(visibility='listed', approved=True) 
        return Disket.objects.all()
    
class DisketShelfView(ListView):
    model = Disket
    template_name = 'disket/list.html'
    context_object_name = 'diskettes'

    def get_queryset(self):
        return Disket.objects.filter(shelf=self.kwargs['shelf'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shelf'] = self.kwargs['shelf']
        return context


def serve_with_x_frame_options(request, path, document_root=None, show_indexes=False):
    response = serve(request, path, document_root, show_indexes)
    response['X-Frame-Options'] = settings.X_FRAME_OPTIONS
    return response
