from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Course, Lesson, Comments
from .serializers import CourseListSerializer, CourseDetailSerializer, LessonListSerializer, CommentSerializer

# view function for getting courses from database and creates get_courses api endpoint for frontend
@api_view(['GET'])
def get_courses(request):
    courses = Course.objects.all()
    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data)

# view function for getting courses from database and displaying them in frontpage
@api_view(['GET'])
def get_frontpage_courses(request):
    courses = Course.objects.all()[0:4]
    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data)

# view function for getting single courses and lesson from django-admin backend 
# and creates get_course api endpiont for frontend using serializers
@api_view(['GET'])
def get_course(request, slug):
    course = Course.objects.get(slug=slug)
    course_serializer = CourseDetailSerializer(course)
    lesson_serializer = LessonListSerializer(course.lessons.all(), many=True)

    data = {
        'course': course_serializer.data,
        'lessons': lesson_serializer.data
    }
    
    return Response(data)

# view function for getting comments from database and creats api endpoint 
# for displaying in frontend
@api_view(['GET'])
def get_comments(request, course_slug, lesson_slug):
    lesson = Lesson.objects.get(slug=lesson_slug)
    serializer = CommentSerializer(lesson.comments.all(), many=True)
    return Response(serializer.data)

# view function that allows comments from User to be stored in database
@api_view(['POST'])
def add_comment(request, course_slug, lesson_slug):
    data = request.data
    name = data.get('name')
    content = data.get('content')

    course = Course.objects.get(slug=course_slug)
    lesson = Lesson.objects.get(slug=lesson_slug)

    comment = Comments.objects.create(course=course, lesson=lesson , name=name, content=content, created_by=request.user)

    serializer = CommentSerializer(comment)

    return Response(serializer.data)
