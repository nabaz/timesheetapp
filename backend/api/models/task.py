from django.db import models
from api.models.project import Project
from django.contrib.auth.models import User

class Task(models.Model):
	STATUS = (
	        ('A', 'Active'),
	        ('IA', 'InActive'),
	        ('C', 'Closed'),
	    )
	name = models.CharField(max_length=200)
	description = models.TextField()
	status = models.CharField(max_length=20, choices = STATUS)
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	user = models.ForeignKey(User)
	created_at = models.DateTimeField(editable=False)
	updated_at = models.DateTimeField()

	def __str__(self):
		return self.name

	class Meta:
		indexes = [
		    models.Index(fields=['name', 'project']),
		]