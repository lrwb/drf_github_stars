from django.db import models


class PythonProjects(models.Model):
    repo_name = models.CharField(max_length=100)
    repo_id = models.IntegerField(unique=True)
    url = models.URLField(max_length=256)
    creation_time = models.DateTimeField(auto_now=False)
    last_push_time = models.DateTimeField(auto_now=False)
    description = models.CharField(max_length=512, blank=True)
    stars = models.PositiveIntegerField(0)

    def __str__(self):
        return (
            f"<PythonProjects(repo_name='{self.repo_name}', "
            f"repo_id='{self.repo_id}', url='{self.url}', "
            f"creation_time='{self.creation_time}', "
            f"last_push_time='{self.last_push_time}', "
            f"description='{self.description}', "
            f"stars='{self.stars}')>\n"
        )
