from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class DashboardTemplateView(TemplateView):

    template_name = 'app/dashboard.html'