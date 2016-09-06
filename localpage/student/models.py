from django.db import models

# Create your models here.
class SchoolYear(models.Model):
	start_of_school_year=models.CharField(max_length=4)
	end_of_school_year=models.CharField(max_length=4)
	def school_year(self):
		school_year="%s - %s"%(self.start_of_school_year, self.end_of_school_year)
		return school_year

	def __unicode__(self):
		return self.school_year()

class Department(models.Model):
	school_year=models.ForeignKey(SchoolYear)
	department=models.CharField(max_length=60)
	def __unicode__(self):
		return self.department

class Semister(models.Model):
	school_year=models.ForeignKey(SchoolYear)
	semister=models.CharField(max_length=15)
	def __unicode__(self):
		return self.semister

class Module(models.Model):
	semister=models.ForeignKey(Semister)
	module=models.CharField(max_length=15)
	def __unicode__(self):
		return self.module

class Instructor(models.Model):
	department=models.ForeignKey(Department)
	first_name=models.CharField(max_length=60)
	middle_name=models.CharField(max_length=60)
	last_name=models.CharField(max_length=60)
	extension_name=models.CharField(max_length=5, blank=True)
	email=models.EmailField()
	def full_name(self):
		full_name="%s %s. %s %s"%(self.first_name, self.middle_name[0], self.last_name, self.extension_name)
		return full_name

	def __unicode__(self):
		return self.full_name()

class Block(models.Model):
	module=models.ForeignKey(Module)
	block_name=models.CharField(max_length=60)
	def __unicode__(self):
		return self.block_name

class Student(models.Model):
	block=models.ForeignKey(Block)
	id_number=models.CharField(max_length=20)
	first_name=models.CharField(max_length=60)
	middle_name=models.CharField(max_length=60)
	last_name=models.CharField(max_length=60)
	extension_name=models.CharField(max_length=5, blank=True)
	def full_name(self):
		full_name="%s %s. %s %s"%(self.first_name, self.middle_name[0], self.last_name, self.extension_name)
		return full_name
	def __unicode__(self):
		return self.full_name()

class Subject(models.Model):
	student=models.ManyToManyField(Student)
	subject_code=models.CharField(max_length=20)
	subject_title=models.CharField(max_length=60)
	lab_units=models.IntegerField(default=0)
	lec_units=models.IntegerField(default=0)
	duration=models.IntegerField(default=54)
	def total_units(self):
		total=self.lab_units+self.lec_units
		return total
	def __unicode__(self):
		return self.subject_title

class SubjectSchedule(models.Model):
	subject=models.ForeignKey(Subject)
	time_start=models.CharField(max_length=8)
	end_time=models.CharField(max_length=8)
	def schedule(self):
		schedule="%s - %s"%(self.time_start, self.end_time)
		return schedule
	def __unicode__(self):
		return self.schedule()


