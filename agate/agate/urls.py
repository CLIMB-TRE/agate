from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'agate'
urlpatterns = [
    path('', TemplateView.as_view(template_name="general/landing_page.html"), name='landing_page'),
    path("ingestion/<str:project>/", views.ingestion_attempt_response),
    path("single/<str:uuid>/", views.single_ingestion_attempt_response),
    path("archive/<str:uuid>/", views.archive_ingestion_attempt),
    path("profile/", views.profile),
    path("projects/", views.projects),
    path("update/", views.update_ingestion_attempt),
]
