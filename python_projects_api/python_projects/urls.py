from django.urls import path
from .apiviews import PythonProjectsList, PythonProjectsDetail, PythonProjectsUpdate

urlpatterns = [
    path("projects/", PythonProjectsList.as_view(), name="projects_list"),
    path("projects/<int:pk>/", PythonProjectsDetail.as_view(), name="projects_detail"),
    path("projects/update/", PythonProjectsUpdate.as_view(), name="projects_update"),
]
