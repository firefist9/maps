from django.urls import path

from .import views

urlpatterns=[
    path('<int:pk>', views.CompanyDetailView.as_view(), name='company_detail'),
]