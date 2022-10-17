from django.urls import path

from .views import UpdateStudentView
from .views import create_student
from .views import delete_student
from .views import detail_student
from .views import get_students

app_name = 'students'

urlpatterns = [
    path('create/', create_student, name='create'),
    path('', get_students, name='list'),
    path('detail/<int:student_id>/', detail_student, name='detail'),
    path('update/<int:pk>/', UpdateStudentView.as_view(), name='update'),
    path('delete/<int:student_id>/', delete_student, name='delete'),
]
