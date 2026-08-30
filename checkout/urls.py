from django.urls import path
from . import views

urlpatterns = [
    path('<int:course_id>/', views.checkout, name='checkout'),
    path('success/<int:course_id>/', views.checkout_success, name='checkout_success'),
]