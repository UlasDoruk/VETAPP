#  ----------- Class based import section ------------- #
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from owners.models import Owners
from anımals.models import Anımals


class OwnersListView(ListView):
    model = Owners
    template_name = "owners.html"
    context_object_name = "owners"


class OwnersDetailView(DetailView):
    # Getting the Owners model from owners/models
    model = Owners
    # Leading the OwnersDetailView class to owner.html
    template_name = "owner.html"
    # We are using "owner" key instead of "object" in owner.html document
    context_object_name = "owner"
    # Taking Anımals objects and adding to owner itself

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['anımals'] = Anımals.objects.filter(available=True, owner=self.kwargs["pk"])
        return context
