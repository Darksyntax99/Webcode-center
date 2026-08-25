from django.urls import path
from . import views 

# Course app URLs.
urlpatterns = [
    path('', views .courses_home, name='courses_home'),
    path('<int:course_id>/', views.course_detail, name = 'course_detail'),
]
