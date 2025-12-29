
from django.urls import path
from . import views

urlpatterns = [
    path("", views.submit_brief, name="submit"),
    path("dashboard/", views.dashboard, name="dashboard"),
]