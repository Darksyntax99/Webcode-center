import stripe
from django.shortcuts import render, get_object_or_404, redirect
from courses.models import Course, Enrollment
from django.conf import settings
from django.contrib.auth.decorators import login_required

# checkout page


@login_required
def checkout(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    # check if course is already purchased
    if Enrollment.objects.filter(
        user=request.user,
        course=course
    ).exists():
        return redirect('my_courses')

    stripe.api_key = settings.STRIPE_SECRET_KEY

    intent = stripe.PaymentIntent.create(
        amount=int(course.price * 100),
        currency=settings.STRIPE_CURRENCY,
        metadata={
            'user_id': request.user.id,
            'course_id': course.id,

        }
    )

    context = {
        'course': course,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': intent.client_secret,
    }
    return render(request, 'checkout/checkout.html', context)

# success page


@login_required
def checkout_success(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    payment_intent_id = request.GET.get('payment_intent')
    stripe.api_key = settings.STRIPE_SECRET_KEY
    intent = stripe.PaymentIntent.retrieve(payment_intent_id)
    if intent.status == 'succeeded':
        Enrollment.objects.get_or_create(
            user=request.user,
            course=course
        )

    context = {
            'course': course,
        }

    return render(request, 'checkout/checkout_success.html', context)
