from django.db import models
from user.models import Users


class Todos(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completion_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
