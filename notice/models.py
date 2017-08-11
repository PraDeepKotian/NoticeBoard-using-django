from django.db import models

# Create your models here.

class Notice(models.Model):
	"""docstring for ClassName"""
	title = models.CharField(max_length=140)
	body = models.TextField()
	date = models.DateTimeField()
	picture = models.FileField()

	def __str__(self):
		return self.title
	
	class Meta:
		ordering = ["-id"]	