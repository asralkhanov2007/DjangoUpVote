from main.models import Upvote
from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView


# Create your views here.

class UpVotePageView(ListView):
    model = Upvote
    paginate_by = 3
    template_name = 'index.html'