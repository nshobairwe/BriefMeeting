from django.db import models
class Meeting(models.Model):
    meeting_name = models.CharField(max_length=200)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    venue = models.CharField(max_length=200)
    purpose = models.TextField(default="No adding")

    def __str__(self):
        return f"{self.meeting_name} ({self.start_date} - {self.end_date})"


class Brief(models.Model):
    name = models.CharField(max_length=100)
    action_item = models.TextField(default="No adding")
    status = models.TextField(blank=True)
    additional_info = models.TextField(default="No adding")
    created_at = models.DateTimeField(auto_now_add=True)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name} – {self.status}"

class AOB(models.Model):
    action_item = models.TextField(default="No adding")
    assigned_to = models.TextField(blank=True)
    status = models.TextField(blank=True)
    additional_info = models.TextField(default="No adding")
    created_at = models.DateTimeField(auto_now_add=True)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f"{self.action_item} – {self.assigned_to}"



class Attendance(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} - {self.designation}"

class Agenda(models.Model):
    Agender_item = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.Agender_item} - {self.owner}"

