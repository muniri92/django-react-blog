from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime


PROFICIENCY = [('Proficient' ,'Proficient'), ('Intermediate', 'Intermediate'), ('Beginning', 'Beginning')]


@python_2_unicode_compatible
class About(models.Model):
	""""""
	title = models.CharField(max_length=250)
	description = models.CharField(max_length=1000)


	def __str__(self):
		return self.title


@python_2_unicode_compatible
class Skill(models.Model):
	""""""
	skill = models.CharField(max_length=100)
	image = models.URLField(max_length=500)
	proficieny = models.CharField(max_length=20, choices=PROFICIENCY, default='Proficient')


	def __str__(self):
		return self.skill


@python_2_unicode_compatible
class Education(models.Model):
	institution = models.CharField(max_length=100)
	degree = models.CharField(max_length=500)
	start_date = models.DateTimeField('Start Date')
	end_date = models.DateTimeField('End Date')


	def __str__(self):
		return self.institution

 
@python_2_unicode_compatible
class Work(models.Model):
	""""""
	company = models.CharField(max_length=100)
	position = models.CharField(max_length=100)
	start_date = models.DateTimeField('Start Date')
	end_date = models.DateTimeField('End Date')


	def __str__(self):
		return self.company


@python_2_unicode_compatible
class WorkDesc(models.Model):
	""""""
	work = models.ForeignKey(Work, related_name='workdesc', on_delete=models.CASCADE)
	job_description = models.CharField(max_length=750)

	def __str__(self):
		return self.job_description

	def __unicode__(self):
		return self.job_description
	









