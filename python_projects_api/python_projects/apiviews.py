from rest_framework.filters import OrderingFilter
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .ingest import get_github_python_stars
from .models import PythonProjects
from .serializers import PythonProjectsSerializer, PythonProjectsListSerializer


class PythonProjectsList(generics.ListAPIView):
    queryset = PythonProjects.objects.all()
    serializer_class = PythonProjectsListSerializer
    filter_backends = (OrderingFilter,)
    ordering_fields = ("stars", "repo_name", "creation_time", "last_push_time")
    ordering = ("-stars",)


class PythonProjectsDetail(generics.RetrieveAPIView):
    queryset = PythonProjects.objects.all()
    serializer_class = PythonProjectsSerializer


class PythonProjectsUpdate(APIView):
    def put(self, request):
        url = "https://api.github.com/search/repositories"
        data = get_github_python_stars(url)
        serializer = PythonProjectsSerializer(instance=data)
        serializer.update(data)
        return Response(serializer.instance, status=status.HTTP_206_PARTIAL_CONTENT)
