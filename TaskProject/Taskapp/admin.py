from django.contrib import admin

from . models import place
from . models import team

admin.site.site_url = "/app/home"

# Register your models here.
admin.site.register(place)
admin.site.register(team)
