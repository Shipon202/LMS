from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Catagory, Course, Lesson, Material, Enrollment, QuestionAnswer
from .serializers import CatagorySerializers, CourseSerializers, LessonSerializers, EnrollmentSerializers, QuestionAnswerSerializers, MaterialSerializers


# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def catagory_list_create(request):
    if request.method == 'GET':
        catagories = Catagory.objects.all()
        serializer = CatagorySerializers(catagories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        if request.user.role != 'admin':
            return Response({'detail': "only admin can create catagories"}, status=403)
        serializer = CatagorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def course_list_create(request):
    if request.method == 'GET':
        if request.user.role in ['admin', 'student']:
            courses == Course.objects.all()
        elif request.user.role  == 'teacher':
            courses = Course.objects.filter(instructor_id=request.user)
        else:
            return Response({'detail': 'unauthorized role'}, status=403)
        serializer = CourseSerializers(courses, many=True)
        return Response(serializer.data)
    

    elif request.method == 'POST':
        if request.user.role != 'teacher':
            return Response({'detail': "only teacher can create courses"}, status=403)
        serializer = CourseSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(instructor_id=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response ({'details': 'please do login !!'})    

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def course_detail(request, pk):
    try :
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response({'detail': 'Course not found'}, status=404)
    if request.method == "GET":
        if request.user.role == 'admin' or request.user == course.instructor_id:
            serializer = CourseSerializers(course)
            return Response(serializer.data)
        return Response({'detail': 'permission denined'}, status=403)
    elif request.method == 'PUT':
        if request.user.role != 'teacher' or request.user != course.instructor_id:
            return Response({'detail': 'only course teacher cna update this course'}, status=403)
        serializer = CourseSerializers(course, data = request.data)
        if serializer.is_valid():
            serializer.save(instructor_id = request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        if request.user.role != 'teacher' or request.user != course.instructor_id:
            return Response({'detail': 'only course teacher cna delete this course'}, status=403)
        course.delete()
        return Response({'detail' : "course deleted"}, status=status.HTTP_204_NO_CONTENT)
    
@api_view (['GET', 'POST'])
@permission_classes([IsAuthenticated])
def lesson_list_create(request):
    if request.method == 'GET':
        catagories = Lesson.objects.all()
        serializer = CatagorySerializers(catagories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LessonSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view (['GET', 'POST'])
@permission_classes([IsAuthenticated])
def meterial_list_create(request):
    if request.method == 'GET':
        catagories = Material.objects.all()
        serializer = MaterialSerializers(catagories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MaterialSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view (['GET', 'POST'])
@permission_classes([IsAuthenticated])
def enrollment_list_create(request):
    if request.method == 'GET':
        catagories = Enrollment.objects.all()
        serializer = EnrollmentSerializers(catagories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EnrollmentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view (['GET', 'POST'])
@permission_classes([IsAuthenticated])
def questionanswer_list_create(request):
    if request.method == 'GET':
        catagories = QuestionAnswer.objects.all()
        serializer = QuestionAnswerSerializers(catagories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = QuestionAnswerSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
