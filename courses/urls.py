from django.urls import path
from . import views 

# Course app URLs.
urlpatterns = [
    path('', views .courses_home, name='courses_home'),
]