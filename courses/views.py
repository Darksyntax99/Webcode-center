from django.shortcuts import render, get_object_or_404
from .models import Course

#show courses page .
def courses_home(request):
    courses = Course.objects.all()

    context = {
        'courses': courses,
    }

    return render(request, 'courses/courses_home.html', context)

#  first course
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    context = {
        'course' : course
    }
    return render(request, 'courses/course_detail.html', context)
