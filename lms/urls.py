"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from core.views import index

from django.contrib import admin
from django.urls import include, path

from groups.views import detail_group, list_groups, update_group

from teachers.views import detail_teacher, list_teachers, update_teacher


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('groups/', list_groups),
    path('groups/detail/<int:group_id>/', detail_group),
    path('groups/update/<int:group_id>/', update_group),
    path('teachers/', list_teachers),
    path('teachers/detail/<int:teacher_id>/', detail_teacher),
    path('teachers/update/<int:teacher_id>/', update_teacher),
    path('students/', include('students.urls')),
]
