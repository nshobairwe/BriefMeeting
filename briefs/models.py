from django.db import models

class Brief(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    tasks = models.TextField()
    challenges = models.TextField()
    suggestions = models.TextField(blank=True)
    ideas = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} – {self.department}"
