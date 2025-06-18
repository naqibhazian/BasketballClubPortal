from django.contrib import admin
from .models import Students, Lecturers, Meetups, Tournament

# Register your models here.
admin.site.register(Students)
admin.site.register(Lecturers)
admin.site.register(Meetups)
admin.site.register(Tournament)
