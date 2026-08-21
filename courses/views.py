from django.shortcuts import render

# Courses.
def courses_home(request):
    return render(request, 'courses/courses_home.html')