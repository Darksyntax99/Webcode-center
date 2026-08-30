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
    path('review/add/<int:course_id>/', views.add_review, name='add_review'),
    path('review/edit/<int:review_id>/', views.edit_review, name='edit_review'),
    path('review/delete/<int:review_id>/', views.delete_review, name='delete_review'),
    path('enroll/<int:course_id>/', views.enroll_course, name='enroll_course' ),
]
