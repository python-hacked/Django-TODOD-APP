from django.db import models
from django.urls import reverse
# Create your models here.
class Create(models.Model):
	title=models.CharField(max_length=200,blank=False)
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('index')
        