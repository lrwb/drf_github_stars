from rest_framework import viewsets   #added this line

from .models import PythonProjects
from .serializers import PythonProjectsSerializer

# Create your views here.

class PythonProjectsViewSet(viewsets.ModelViewSet):
    queryset = PythonProjects.objects.all()
    serializer_class = PythonProjectsSerializer
