
from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("action_item/", views.submit_brief, name="submit"),
    path("aob/", views.submit_aob, name="submit_aob"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("", views.create_meeting, name="create_meeting"),
    path("meeting/attendees/", views.add_attendance, name="add_attendance"),
    path("logout/", views.logout_view, name="logout"), 
    path("report/", views.generate_report, name="generate_report"),

]