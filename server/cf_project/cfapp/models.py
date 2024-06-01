from django.db import models
class CostModel(models.Model):
	name = models.CharField(max_length=50, primary_key=True)
	cost = models.FloatField(default=0.0)

	def __str__(self):
		return self.name
