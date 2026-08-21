from django.contrib import admin
from .models import Course

# Add courses to admin.
admin.site.register(Course)