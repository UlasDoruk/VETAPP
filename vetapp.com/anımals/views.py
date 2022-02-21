#  ----------- Class based import section ------------- #
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from anımals.models import Anımals


class AnımalsListView(ListView):
    model = Anımals
    template_name = "anımals.html"
    context_object_name = "anımals"


class AnımalsDetailView(DetailView):
    # Getting the Anımals model from anımals/models
    model = Anımals
    # Leading the AnımalsDetailView class to anımal.html
    template_name = "anımals.html"
    # We are using "anımal" key instead of "object" in anımal.html document
    context_object_name = "anımal"
    # Taking Anımals objects and adding to anımal itself
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['anımals'] = Anımals.objects.filter(available=True, id=self.kwargs["pk"])
        return context

