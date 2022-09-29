from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render

from .forms import UpdateGroupForm
from .models import Group


def list_groups(request):
    groups = Group.objects.all()
    return render(request, 'groups/list.html', {'title': 'List of groups', 'groups': groups})


def detail_group(request, group_id):
    group = Group.objects.get(pk=group_id)
    return render(request, 'groups/detail.html', {'title': 'Group details', 'group': group})


def update_group(request, group_id):
    group = Group.objects.get(pk=group_id)

    if request.method == 'GET':
        form = UpdateGroupForm(instance=group)
    elif request.method == 'POST':
        form = UpdateGroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')

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
