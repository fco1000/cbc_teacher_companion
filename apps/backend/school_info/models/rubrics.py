from django.db import models
from .school import LearningArea,year,term
from .strands import Strand
from django.utils import timezone

class AuthenticAssessmentRubric(models.Model):
    term = models.CharField(choices=term,max_length=100)
    year = models.CharField(choices=year,max_length=100)
    learning_area = models.ForeignKey(LearningArea,on_delete=models.CASCADE)
    strand = models.ForeignKey(Strand,on_delete=models.CASCADE)
    task = models.CharField(max_length=150)
    date = models.DateField(timezone.now())
    criteria = models.TextField(max_length=500)
    exceeds_expectations = models.TextField(max_length=500)
    meets_expectations = models.TextField(max_length=500)
    approaches_expectations = models.TextField(max_length=500)
    below_expectations = models.TextField(max_length=500)
 
    def __str__(self):
        return self.task

class ProjectRubric(models.Model):
    term = models.CharField(choices=term,max_length=100)
    year = models.CharField(choices=year,max_length=100)
    learning_area = models.ForeignKey(LearningArea,on_delete=models.CASCADE)
    strand = models.ForeignKey(Strand,on_delete=models.CASCADE)
    skills_tested = models.TextField(max_length=500)
    values_to_be_learned = models.TextField(max_length=500)