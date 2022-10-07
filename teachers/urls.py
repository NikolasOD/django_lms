from django.urls import path

from .views import create_teacher
from .views import delete_teacher
from .views import detail_teacher
from .views import list_teachers
from .views import update_teacher

app_name = 'teachers'

urlpatterns = [
    path('create/', create_teacher, name='create'),
    path('', list_teachers, name='list'),
    path('detail/<int:teacher_id>/', detail_teacher, name='detail'),
    path('update/<int:teacher_id>/', update_teacher, name='update'),
    path('delete/<int:teacher_id>/', delete_teacher, name='delete'),
]
