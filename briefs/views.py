from django.shortcuts import render, redirect
from .models import Brief
from .forms import BriefForm
from django.db.models import Count

def submit_brief(request):
    form = BriefForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("thanks")
    return render(request, "submit.html", {"form": form})


def dashboard(request):
    briefs = Brief.objects.order_by("-created_at")

    challenges = (
        Brief.objects.values("challenges")
        .exclude(challenges="")
        .annotate(total=Count("challenges"))
        .filter(total__gt=1)
    )

    return render(request, "dashboard.html", {
        "briefs": briefs,
        "challenges": challenges
    })
