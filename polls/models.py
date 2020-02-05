from django.db import models

# Create your models here.
class Question(models.Model):
	qtext = models.CharField(max_length = 200)
	pdate = models.DateTimeField('date published')
	
	def __str__(self):
		return self.qtext
		
	def was_published_recently(self):
		return self.pdate >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	choiceText = models.CharField(max_length = 200)
	votes = models.IntegerField(default = 0)
	
	def __str__(self):
		return self.choiceText
