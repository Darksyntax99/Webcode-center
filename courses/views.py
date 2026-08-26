from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .forms import CourseForm

#show courses page.
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

# view my.courses 
def my_courses(request):
    return render(request, 'courses/my_courses.html')
# Add new course
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('courses_home')
    else:
            form = CourseForm()

            context = {
                'form': form
            }
            return render(request, 'courses/add_course.html', context)