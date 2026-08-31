from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Course, Review, Enrollment
from .forms import CourseForm, ReviewForm


# show courses page.
def courses_home(request):
    courses = Course.objects.all()

    context = {
        'courses': courses,
    }

    return render(request, 'courses/courses_home.html', context)


# course deatils
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    is_enrolled = False

    if request.user.is_authenticated:
        is_enrolled = Enrollment.objects.filter(
              user=request.user,
              course=course
         ).exists()

    context = {
        'course': course,
        'is_enrolled': is_enrolled
    }

    return render(request, 'courses/course_detail.html', context)


# My courses
@login_required
def my_courses(request):
    enrollments = Enrollment.objects.filter(user=request.user)
    context = {
        'enrollments': enrollments,
    }

    return render(request, 'courses/my_courses.html', context)


# Add new course
@staff_member_required
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
@staff_member_required
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


@staff_member_required
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
@login_required
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


@login_required
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

# Delete review


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(
        Review,
        id=review_id,
        user=request.user
    )

    if request.method == 'POST':
        course_id = review.course.id
        review.delete()

        return redirect(
               'course_detail',
               course_id=course_id
        )

    context = {
        'review': review
    }

    return render(request, 'courses/delete_review.html', context)
