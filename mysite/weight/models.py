from django.db import models

# Create your models here.

class Stock(models.Model):
	paper_roll_id = models.CharField(max_length=4)
	paper_code = models.CharField(max_length=6)
	initial_weight = models.FloatField(max_length=4)
	temp_weight = models.FloatField(max_length=4)

class Movement(models.Model):
	movement_id = models.IntegerField(max_length=11)
	paper_roll_id = models.CharField(max_length=4)
	from_weight = models.FloatField(max_length=4)
	to_weight = models.FloatField(max_length=4)
	up_datetime = models.DateTimeField()

class Rollback(models.Model):
	datetime = models.DateTimeField()
	temp_weight = models.FloatField(max_length=4)
	paper_roll_id = models.CharField(max_length=4)
	paper_code = models.CharField(max_length=6)
	current_weight = models.FloatField(max_length=4)
	undo_weight = models.FloatField(max_length=4)


