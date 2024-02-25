from django.contrib import admin
from .models import *
# Register your models here.
class CircuitAdmin(admin.ModelAdmin):
  list_display = ['name','gif','image']


admin.site.register(Circuit, CircuitAdmin)