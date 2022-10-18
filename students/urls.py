from django.urls import path

from .views import CreateStudentView
from .views import DeleteStudentView
from .views import DetailStudentView
from .views import UpdateStudentView
from .views import get_students

app_name = 'students'

urlpatterns = [
    path('create/', CreateStudentView.as_view(), name='create'),
    path('', get_students, name='list'),
    path('detail/<int:pk>/', DetailStudentView.as_view(), name='detail'),
    path('update/<int:pk>/', UpdateStudentView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteStudentView.as_view(), name='delete'),
]
