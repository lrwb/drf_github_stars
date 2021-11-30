from rest_framework import serializers

from .models import PythonProjects


class PythonProjectsSerializer(serializers.ModelSerializer):
    def update_or_create_python_projects(self, item):
        updates = {
            "repo_name": item.get("repo_name", None),
            "url": item.get("url", None),
            "creation_time": item.get("creation_time", None),
            "last_push_time": item.get("last_push_time", None),
            "description": item.get("description", "Alpha"),
            "stars": item.get("stars", 0),
        }
        project, created = PythonProjects.objects.update_or_create(
            repo_id=item.get("repo_id", None), defaults=updates
        )
        return project

    def update(self, validated_data):
        if isinstance(validated_data, list):
            project = []
            for item in validated_data:
                resp = self.update_or_create_python_projects(item)
                project.append(resp)
        elif isinstance(validated_data, dict):
            project = self.update_or_create_python_projects(validated_data)
        return project

    class Meta:
        model = PythonProjects
        fields = "__all__"


class PythonProjectsListSerializer(PythonProjectsSerializer):
    def to_representation(self, instance):
        representation = {
            "id": instance.id,
            "repo_name": instance.repo_name,
            "description": instance.description,
        }
        return representation
