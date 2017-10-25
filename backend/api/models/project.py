from django.db import models
from api.models.customer import Customer
from django.contrib.auth.models import User

class Project(models.Model):
	STATUS = (
	        ('A', 'Active'),
	        ('IA', 'InActive'),
	        ('C', 'Closed'),
	    )

	name = models.CharField(max_length=200)
	description = models.TextField()
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	user = models.ManyToManyField(User)
	created_at = models.DateTimeField(editable=False)
	updated_at = models.DateTimeField()
	status = models.CharField(max_length=20, choices = STATUS)

	def __str__(self):
		return self.name


	class Meta:
	    indexes = [
            models.Index(fields=['name', 'customer']),
        ]