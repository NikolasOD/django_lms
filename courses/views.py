from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import CreateCourseForm, CourseFilterForm, UpdateCourseForm
from .models import Course


def list_courses(request):
    courses = Course.objects.all()

    filter_form = CourseFilterForm(data=request.GET, queryset=courses)

    return render(request, 'courses/list.html', {'filter_form': filter_form})


def detail_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'courses/detail.html', {'course': course})


def create_course(request):
    if request.method == 'GET':
        form = CreateCourseForm()
    elif request.method == 'POST':
        form = CreateCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:list'))

    return render(request, 'courses/create.html', {'form': form})


def update_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.method == 'GET':
        form = UpdateCourseForm(instance=course)
    elif request.method == 'POST':
        form = UpdateCourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:list'))

    return render(request, 'courses/update.html', {'form': form, 'course': course})


def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.method == 'POST':
        course.delete()
        return HttpResponseRedirect(reverse('courses:list'))

    return render(request, 'courses/delete.html', {'course': course})
