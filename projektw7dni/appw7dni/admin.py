from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Employee)
admin.site.register(HourTableStart)
admin.site.register(HourTableEnd)