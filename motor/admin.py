from django.contrib import admin
from .models import Motor

# Register your models here.

# @admin.register(Motor)
# class AdminMotor(admin.ModelAdmin):
#     list_display: ['nama', 'plat']

admin.site.register(Motor)