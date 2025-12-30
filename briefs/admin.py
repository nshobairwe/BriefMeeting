from django.contrib import admin
from .models import Meeting, Brief, AOB, Attendance, Agenda

admin.site.register(Meeting)
admin.site.register(Brief)
admin.site.register(AOB)
admin.site.register(Attendance)
admin.site.register(Agenda)
