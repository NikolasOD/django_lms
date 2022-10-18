from django.urls import path

from .views import CreateTeacherView
from .views import DeleteTeacherView
from .views import DetailTeacherView
from .views import UpdateTeacherView
from .views import list_teachers

app_name = 'teachers'

urlpatterns = [
    path('create/', CreateTeacherView.as_view(), name='create'),
    path('', list_teachers, name='list'),
    path('detail/<int:pk>/', DetailTeacherView.as_view(), name='detail'),
    path('update/<int:pk>/', UpdateTeacherView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteTeacherView.as_view(), name='delete'),
]
