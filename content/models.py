from django.db import models


# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=50)
    module = models.CharField(max_length=2)
    students = models.IntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'([{self.id}] {self.title} - {self.modules})'
