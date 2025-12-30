from django.shortcuts import render, redirect
from .models import Brief,AOB, Meeting, Attendance, Agenda
from .forms import MeetingForm, AttendanceForm
from .forms import BriefForm, AOBForm
from django.db.models import Count
from django.contrib.auth import authenticate, login, logout
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("create_meeting")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")

def submit_brief(request):
    form = BriefForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("dashboard")
    return render(request, "items_action.html", {"form": form})

def submit_aob(request):
    form = AOBForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("dashboard")
    return render(request, "aob.html", {"form": form})

def dashboard(request):
    briefs = Brief.objects.all().order_by("-created_at")
    aob = AOB.objects.all().order_by("-created_at")
    meetings = Meeting.objects.all().order_by("-start_date")
    attendance = Attendance.objects.all()
    agendas = Agenda.objects.all()

    return render(request, "dashboard.html", {
        "briefs": briefs,
        "aob": aob,
        "meetings": meetings,
        "attendance": attendance,
        "agendas": agendas
    })

def create_meeting(request):
    if request.method == "POST":
        meeting_form = MeetingForm(request.POST)
        if meeting_form.is_valid():
            meeting = meeting_form.save()
            request.session["meeting_id"] = meeting.id
            return redirect("submit")
    else:
        meeting_form = MeetingForm()
    return render(request, "create_meeting.html", {"form": meeting_form})


def add_attendance(request):
    # meeting_id = request.session.get("meeting_id")
    # if not meeting_id:
    #     return redirect("create_meeting")

    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            att = form.save(commit=False)
            att.meeting_id = meeting_id
            att.save()
            return redirect("add_attendance")
    else:
        form = AttendanceForm()

    # attendees = Attendance.objects.filter(meeting_id=meeting_id)
    return render(request, "add_attendance.html", {"form": form})

def generate_report(request):
    context = {
        "meetings": Meeting.objects.all(),
        "attendance": Attendance.objects.all(),
        "agendas": Agenda.objects.all(),
        "briefs": Brief.objects.all(),
        "aob": AOB.objects.all(),
    }

    template = get_template("dashboard.html")
    html = template.render(context)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "attachment; filename=Meeting_Report.pdf"

    pisa.CreatePDF(html, dest=response)
    return response

def logout_view(request):
    logout(request)
    return redirect("login")