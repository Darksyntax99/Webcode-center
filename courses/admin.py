from django.contrib import admin
from .models import Course, Lesson

# Add courses to admin.
admin.site.register(Course)
admin.site.register(Lesson)
