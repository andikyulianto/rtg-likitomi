from django.db import models

# Create your models here.

#class Stock(models.Model):
#	paper_roll_id = models.CharField(max_length=4)
#	paper_code = models.CharField(max_length=6)
#	initial_weight = models.FloatField(max_length=4)
#	temp_weight = models.FloatField(max_length=4)

#class Movement(models.Model):
#	movement_id = models.IntegerField(max_length=11)
#	paper_roll_id = models.CharField(max_length=4)
#	from_weight = models.FloatField(max_length=4)
#	to_weight = models.FloatField(max_length=4)
#	up_datetime = models.DateTimeField()

#class Rollback(models.Model):
#	datetime = models.DateTimeField()
#	temp_weight = models.FloatField(max_length=4)
#	paper_roll_id = models.CharField(max_length=4)
#	paper_code = models.CharField(max_length=6)
#	current_weight = models.FloatField(max_length=4)
#	undo_weight = models.FloatField(max_length=4)

class ClampliftPlan(models.Model):
	date = models.DateField()
	start_time = models.TimeField()
	end_time = models.TimeField()
	sheet_code = models.CharField(max_length=6)
	customer_name = models.CharField(max_length=64)
	product = models.CharField(max_length=64)
	sono = models.CharField(max_length=5)
	ordno = models.CharField(max_length=6)
	flute = models.CharField(max_length=1)
	df = models.CharField(max_length=6)
	bl = models.CharField(max_length=6)
	bm = models.CharField(max_length=6)
	cl = models.CharField(max_length=6)
	cm = models.CharField(max_length=6)
	paper_width_mm = models.PositiveIntegerField()
	paper_width_inch = models.PositiveIntegerField()
	length_df = models.PositiveIntegerField()
	length_bl = models.PositiveIntegerField()
	length_bm = models.PositiveIntegerField()
	length_cl = models.PositiveIntegerField()
	length_cm = models.PositiveIntegerField()
	actual_df = models.PositiveIntegerField()
	actual_bl = models.PositiveIntegerField()
	actual_bm = models.PositiveIntegerField()
	actual_cl = models.PositiveIntegerField()
	actual_cm = models.PositiveIntegerField()
	loss_df = models.PositiveIntegerField()
	loss_bl = models.PositiveIntegerField()
	loss_bm = models.PositiveIntegerField()
	loss_cl = models.PositiveIntegerField()
	loss_cm = models.PositiveIntegerField()
	sheet_length = models.PositiveIntegerField()
	case = models.PositiveIntegerField()
	cut = models.PositiveIntegerField()

	def __str__(self):
		return self.sheet_code

#	def __unicode__(self):
#		return u'%s, %s' % (self.start_time, self.end_time)

	class Meta:
		ordering = ['-date', 'start_time']

	class Admin:
		list_display = ('case', 'cut')



