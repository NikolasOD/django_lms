from django.urls import path

from .views import DeleteGroupView
from .views import DetailGroupView
from .views import ListGroupView
from .views import UpdateGroupView
from .views import create_group

app_name = 'groups'

urlpatterns = [
    path('create/', create_group, name='create'),
    path('', ListGroupView.as_view(), name='list'),
    path('detail/<int:pk>/', DetailGroupView.as_view(), name='detail'),
    path('update/<int:pk>/', UpdateGroupView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteGroupView.as_view(), name='delete'),
]
