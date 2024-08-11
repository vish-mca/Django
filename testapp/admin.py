from .models import Employee 
from django.contrib import admin

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=['name','marks']

admin.site.register(Employee,StudentAdmin)