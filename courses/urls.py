from django.urls import path

from .views import CreateStudentView
from .views import DeleteStudentView
from .views import DetailCourseView
from .views import ListCourseView
from .views import UpdateStudentView

app_name = 'courses'

urlpatterns = [
    path('create/', CreateStudentView.as_view(), name='create'),
    path('', ListCourseView.as_view(), name='list'),
    path('detail/<int:pk>/', DetailCourseView.as_view(), name='detail'),
    path('update/<int:pk>/', UpdateStudentView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteStudentView.as_view(), name='delete'),
]
