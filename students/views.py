from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView,  DetailView, UpdateView

from .forms import CreateStudentForm, StudentFilterForm
from .forms import UpdateStudentForm
from .models import Student


def get_students(request):
    students = Student.objects.select_related('group')

    filter_form = StudentFilterForm(data=request.GET, queryset=students)

    return render(request, 'students/list.html', {'filter_form': filter_form})


class DetailStudentView(DetailView):
    model = Student
    template_name = 'students/detail.html'


class CreateStudentView(CreateView):
    model = Student
    form_class = CreateStudentForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/create.html'


class UpdateStudentView(UpdateView):
    model = Student
    form_class = UpdateStudentForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'


class DeleteStudentView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list')
    template_name = 'students/delete.html'
