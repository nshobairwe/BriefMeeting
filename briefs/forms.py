from django import forms
from .models import Brief, AOB, Meeting, Attendance

class BriefForm(forms.ModelForm):
    class Meta:
        model = Brief
        fields = "__all__"

class AOBForm(forms.ModelForm):
    class Meta:
        model = AOB
        fields = "__all__"

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = "__all__"

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ["name", "designation"]