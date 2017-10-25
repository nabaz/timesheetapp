from django.db import models
from django.utils import timezone

class Customer(models.Model):
	STATUS = (
        ('A', 'Active'),
        ('IA', 'InActive'),
        ('C', 'Closed'),
    )

	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	note = models.TextField()
	status = models.CharField(max_length=20, choices = STATUS)
	created_at = models.DateTimeField(editable=False)
	updated_at = models.DateTimeField()

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
	        ''' On save, update timestamps '''
	        if not self.id:
	            self.created_at = timezone.now()
	        self.updated_at = timezone.now()
	        return super(Customer, self).save(*args, **kwargs)
