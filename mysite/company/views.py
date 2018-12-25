from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Company

class CompanyDetailView(DetailView):
    model=Company
    template_name='company_detail.html'
