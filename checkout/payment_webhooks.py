from courses.models import Course, Enrollment
from django.contrib.auth.models import User
from django.http import HttpResponse

class PaymentWebhook:
    """Payment webhooks."""
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

    def payment_succeeded(self, event):
        intent= event.data.object

        user_id = intent.metadata.user_id
        course_id = intent.metadata.course_id

        user = User.objects.get(id=user_id)
        course = Course.objects.get(id=course_id)

        Enrollment.objects.get_or_create(
            user=user,
            course=course
        )
        return HttpResponse(
            content='Payment Succeeded',
            status=200
        )
    def payment_failed(self, event):
        return HttpResponse(
            content= 'Payment failed',
            status=200
        )