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

#   course deatils
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    context = {
        'course' : course
    }
    return render(request, 'courses/course_detail.html', context)

# My courses 
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
# Edit course
def edit_course(request, course_id):
     course = get_object_or_404(Course, id=course_id)
     if request.method == 'POST':
          form = CourseForm(request.POST, instance=course)

          if form.is_valid():
               form.save()
               return redirect('course_detail', course_id=course.id)
     else:
          form = CourseForm(instance=course)
     context = {
          'form': form,
          'course': course 
     }
     return render(request, 'courses/edit_course.html', context)

# delete course 
def delete_course(request, course_id):
     course = get_object_or_404(Course, id=course_id)

     if request.method == 'POST':
          course.delete()
          return redirect('courses_home')
     context = {
          'course': course
     }
     return render(request, 'courses/delete_course.html', context)


