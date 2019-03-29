from django.contrib import admin

from .models import Course, Step
class StepInline(admin.TabularInline):
    model = Step

class CourseAdmin(admin.ModelAdmin):
    inlines = [
        StepInline,
    ]
admin.site.register(Course, CourseAdmin)

# Register your models here.

