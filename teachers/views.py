from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from .forms import CreateTeacherForm, TeacherFilterForm, UpdateTeacherForm
from .models import Teacher


def list_teachers(request):
    teachers = Teacher.objects.all()

    filter_form = TeacherFilterForm(data=request.GET, queryset=teachers)

    return render(request, 'teachers/list.html', {'filter_form': filter_form})


class DetailTeacherView(DetailView):
    model = Teacher
    template_name = 'teachers/detail.html'


class CreateTeacherView(CreateView):
    model = Teacher
    form_class = CreateTeacherForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/create.html'


class UpdateTeacherView(UpdateView):
    model = Teacher
    form_class = UpdateTeacherForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/update.html'


class DeleteTeacherView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/delete.html'
