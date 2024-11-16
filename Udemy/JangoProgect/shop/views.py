from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Course


def index(reqest):
    courses = Course.objects.all()
    return render(reqest, 'shop/courses.html', context={'courses': courses})


def single_course(reqest, course_id):
    # OPTION 1
    # try:
    #     course = Course.objects.get(pk=course_id)
    #     return render(reqest, 'single_course.html', {'course': course})
    # except Course.DoesNotExist:
    #     raise Http404()

    # OPTION 2
    course = get_object_or_404(Course, pk=course_id)
    return render(reqest, 'shop/single_course.html', {'course': course})
