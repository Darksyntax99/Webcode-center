from django.urls import path
from . import views
from .webhook_views import stripe_webhook

urlpatterns = [
    path('<int:course_id>/', views.checkout, name='checkout'),
    path('success/<int:course_id>/', views.checkout_success, name='checkout_success'),
    path('webhook/', stripe_webhook, name='stripe_webhook'),
]