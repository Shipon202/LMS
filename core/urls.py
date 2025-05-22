from django.urls import path
from .views import catagory_list_create, course_list_create, course_detail, lesson_list_create, meterial_list_create, enrollment_list_create, questionanswer_list_create
urlpatterns = [
    path('catagories/', catagory_list_create, name='catagory_list_create'),
    path('courses/', course_list_create, name='course_list_create'),
    path('course/<int:pk>/', course_detail, name='course_detail'),
    path('lessons/', lesson_list_create, name='lesson_list_create'),
    path('meterials/', meterial_list_create, name='meterial_list_create'),
    path('enrollments/', enrollment_list_create, name='enrollment_list_create'),
    path('questions/', questionanswer_list_create, name='questionanswer_list_create'),
]
