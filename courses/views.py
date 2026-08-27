from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Review
from .forms import CourseForm, ReviewForm


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


# Add review
def add_review(request, course_id):
     course = get_object_or_404(Course, id=course_id)

     if request.method == 'POST':
          form = ReviewForm(request.POST)

          if form.is_valid():
               review = form.save(commit=False)
               review.user = request.user
               review.course = course
               review.save()

               return redirect('course_detail', course_id=course.id)
     else:
          form = ReviewForm()

     context = {
          'form': form,
          'course': course
     }
     return render(request, 'courses/add_review.html', context)

# Edit review
def edit_review(request, review_id):
     review = get_object_or_404(
          Review, 
          id=review_id,
          user=request.user
     )
     if request.method == 'POST':
          form = ReviewForm(request.POST, instance=review)

          if form.is_valid():
               form.save()
               return redirect(
                    'course_detail',
                    course_id=review.course.id
               )
     else:
          form = ReviewForm(instance=review)
          context = {
                   'form': form,
                   'review': review
              }

     return render(request, 'courses/edit_review.html', context)
