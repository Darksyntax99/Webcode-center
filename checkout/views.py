import stripe 
from django.shortcuts import render, get_object_or_404
from courses.models import Course
from django.conf import settings

# Create your views here.
def checkout(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    stripe.api_key = settings.STRIPE_SECRET_KEY
    intent = stripe.PaymentIntent.create(
        amount=round(course.price * 100),
        currency= setting.STRIPE_CURRENCY
    )

    context ={
        'course': course,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret' : intent.client_secret,
    }
    return render(request, 'checkout/checkout.html', context)
