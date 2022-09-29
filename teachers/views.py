from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render

from .forms import UpdateTeacherForm
from .models import Teacher


def list_teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers/list.html', {'title': 'List of teachers', 'teachers': teachers})


def detail_teacher(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    return render(request, 'teachers/detail.html', {'title': 'Teacher details', 'teacher': teacher})


def update_teacher(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)

    if request.method == 'GET':
        form = UpdateTeacherForm(instance=teacher)
    elif request.method == 'POST':
        form = UpdateTeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')

    token = get_token(request)
    html_form = f'''
        <form method="post">
          <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
          <table>
            {form.as_table()}
          </table>
          <input type="submit" value="Submit">
        </form>
    '''

    return HttpResponse(html_form)
