import stripe

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .payment_webhooks import PaymentWebhook


@require_POST
@csrf_exempt
def stripe_webhook(request):

    payload = request.body
    signature = request.META.get('HTTP_STRIPE_SIGNATURE')

    try:
        event = stripe.Webhook.construct_event(
            payload,
            signature,
            settings.STRIPE_WH_SECRET
        )

    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)

    handler = PaymentWebhook(request)

    event_map = {
        'payment_intent.succeeded': handler.payment_succeeded,
        'payment_intent.payment_failed': handler.payment_failed,
    }

    event_handler = event_map.get(
        event['type'],
        handler.handle_event
    )
    return event_handler(event)
