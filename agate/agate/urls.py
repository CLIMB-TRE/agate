from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'agate'
urlpatterns = [
    path('', TemplateView.as_view(template_name="general/landing_page.html"), name='landing_page'),
    path("ingestion/", views.IngestionAPIView.as_view(), name="ingestion"),
    path("single/<str:uuid>/", views.single_ingestion_attempt_response, name="single"),
    path("archive/<str:uuid>/", views.archive_ingestion_attempt, name="archive"),
    path("delete/<str:uuid>/", views.delete_ingestion_attempt, name="delete"),
    path("profile/", views.profile, name="profile"),
    path("projects/", views.projects, name="projects"),
    path("update/", views.update_ingestion_attempt, name="update"),
]
