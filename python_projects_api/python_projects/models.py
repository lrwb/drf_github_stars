from django.db import models
from django.contrib.auth.models import User

class PythonProjects(models.Model):
    repo_name = models.CharField(max_length=100)
    repo_id = models.IntegerField(unique=True)
    url = models.URLField(max_length=256)
    creation_time = models.DateTimeField(auto_now=False)
    last_push_time = models.DateTimeField(auto_now=False)
    description = models.CharField(max_length=512, blank=True)
    stars = models.PositiveIntegerField(0)

    def __str__(self):
        return ("<PythonProjects(repo_name='{0}', repo_id='{1}', url='{2}', "
                "creation_time='{3}', last_push_time='{4}', description='{5}', "
                "stars='{6}')>\n"
                .format(self.repo_name,
                        self.repo_id,
                        self.url,
                        self.creation_time,
                        self.last_push_time,
                        self.description,
                        self.stars))
