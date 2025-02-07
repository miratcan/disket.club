from django.views.generic import DetailView
from disket.models import Disket
from django.contrib.auth.models import User


class ProfileView(DetailView):
    model = User
    template_name = 'protile/detail.html'
    context_object_name = 'profile'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['diskettes'] = Disket.objects.filter(author=self.object)
        return context