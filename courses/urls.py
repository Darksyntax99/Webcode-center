from django.urls import path
from . import views 

# Course app URLs.
urlpatterns = [
    path('', views .courses_home, name='courses_home'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('my-courses/', views.my_courses, name="my_courses"),
    path('add/', views.add_course, name='add_course'),
    path('edit/<int:course_id>/', views.edit_course, name='edit_course'),
    path('delete/<int:course_id>/', views.delete_course, name='delete_course'),
]
