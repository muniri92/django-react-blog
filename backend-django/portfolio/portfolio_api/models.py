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
class Education(models.Model):
	""""""
	institution = models.CharField(max_length=100)
	major = models.CharField(max_length=100, blank=True, default=None)
	minor = models.CharField(max_length=250, blank=True, default=None)
	certificate = models.CharField(max_length=250, blank=True, default=None)
	start_date = models.DateField('Start Date')
	end_date = models.DateField('End Date')


	def __str__(self):
		return self.institution


@python_2_unicode_compatible
class Certificate(models.Model):
	""""""
	institution = models.CharField(max_length=100)
	certificate = models.CharField(max_length=250)
	start_date = models.DateField('Start Date')
	end_date = models.DateField('End Date')


	def __str__(self):
		return self.certificate


@python_2_unicode_compatible
class SkillSet(models.Model):
	""""""
	skill = models.CharField(max_length=50)

	def __str__(self):
		return self.skill


@python_2_unicode_compatible
class SkillType(models.Model):
	""""""
	skillset = models.ForeignKey(SkillSet, related_name='skilltype', on_delete=models.CASCADE)
	skill = models.CharField(max_length=100)

	def __str__(self):
		return self.skill

	def __unicode__(self):
		return self.skill

 
@python_2_unicode_compatible
class Work(models.Model):
	""""""
	company = models.CharField(max_length=100)
	position = models.CharField(max_length=100)
	start_date = models.DateField('Start Date')
	end_date = models.DateField('End Date')


	def __str__(self):
		return self.company + ', ' + self.position


@python_2_unicode_compatible
class WorkDesc(models.Model):
	""""""
	work = models.ForeignKey(Work, related_name='workdesc', on_delete=models.CASCADE)
	job_description = models.CharField(max_length=750)

	def __str__(self):
		return self.job_description

	def __unicode__(self):
		return self.job_description
	









