from django.db import models
from django.contrib.auth.models import User
from api.models.task import Task 

class TimeEntry(models.Model):
	STATUS = (
	        ('A', 'Active'),
	        ('IA', 'InActive'),
	        ('C', 'Closed'),
	    )
	name = models.CharField(max_length=200)
	description = models.TextField()
	status = models.CharField(max_length=20, choices = STATUS)
	user = models.ForeignKey(User)
	task = models.ForeignKey(Task)
	start_time =  models.DateTimeField(editable=False)
	end_time =  models.DateTimeField(editable=False)
	created_at = models.DateTimeField(editable=False)
	updated_at = models.DateTimeField()

	def __str__(self):
		return self.name

	class Meta:
	    indexes = [
            models.Index(fields=['name', 'user_id', 'task_id']),
        ]