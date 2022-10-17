from django.urls import path

from .views import ListGroupView
from .views import UpdateGroupView
from .views import create_group
from .views import delete_group
from .views import detail_group

app_name = 'groups'

urlpatterns = [
    path('create/', create_group, name='create'),
    path('', ListGroupView.as_view(), name='list'),
    path('detail/<int:group_id>/', detail_group, name='detail'),
    path('update/<int:pk>/', UpdateGroupView.as_view(), name='update'),
    path('delete/<int:group_id>/', delete_group, name='delete'),
]
