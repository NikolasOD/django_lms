from django.urls import path

from .views import CreateTeacherView
from .views import DeleteTeacherView
from .views import DetailTeacherView
from .views import ListTeacherView
from .views import UpdateTeacherView

app_name = 'teachers'

urlpatterns = [
    path('create/', CreateTeacherView.as_view(), name='create'),
    path('', ListTeacherView.as_view(), name='list'),
    path('detail/<int:pk>/', DetailTeacherView.as_view(), name='detail'),
    path('update/<int:pk>/', UpdateTeacherView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteTeacherView.as_view(), name='delete'),
]
