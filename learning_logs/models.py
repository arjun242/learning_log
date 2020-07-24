from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
	text=models.CharField(max_length=200)
	date_added=models.DateTimeField(auto_now_add=True)

	owner = models.ForeignKey(User,on_delete=models.PROTECT)

	def __str__(self):
		'''return text'''
		return self.text

#entries for added topics chess,rockclimbing
class Entry(models.Model):
	'''something specific about topic'''
	topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
	text = models.TextField()
	date_added=models.DateTimeField(auto_now_add=True)
	
	class Meta:
		verbose_name_plural='entries'
	def __str__(self):
		'''return string rep of model'''
		return self.text[:50]+'...'
