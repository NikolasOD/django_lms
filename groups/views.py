from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from webargs.djangoparser import use_args
from webargs.fields import Str

from .forms import CreateGroupForm, UpdateGroupForm
from .models import Group


@use_args(
    {
        'group_name': Str(required=False),
        'group_description': Str(required=False),
    },
    location='query'
)
def list_groups(request, args):
    groups = Group.objects.all()

    if len(args) != 0 and args.get('group_name') or args.get('group_description'):
        groups = groups.filter(
            Q(group_name=args.get('group_name', '')) | Q(group_description=args.get('group_description', ''))
        )

    return render(request, 'groups/list.html', {'groups': groups})


def detail_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    return render(request, 'groups/detail.html', {'group': group})


def create_group(request):
    if request.method == 'GET':
        form = CreateGroupForm()
    elif request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/create.html', {'form': form})


def update_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)

    if request.method == 'GET':
        form = UpdateGroupForm(instance=group)
    elif request.method == 'POST':
        form = UpdateGroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/update.html', {'form': form, 'group': group})


def delete_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)

    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/delete.html', {'group': group})
