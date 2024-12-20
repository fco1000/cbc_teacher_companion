from django.db import models
from .school import (
    LearningArea,
    grade,
    term,
    year,
    remark,
    SummativeType
)
from .strands import Strand, Sub_strand
from django.utils import timezone
from teacher.models import User

class ClassActivitie(models.Model):
    grade = models.CharField(choices=grade,max_length=100)
    learning_area = models.ForeignKey(LearningArea,on_delete=models.CASCADE,null=True)
    strand = models.ForeignKey(Strand,on_delete=models.CASCADE,null=True)
    sub_strand = models.ForeignKey(Sub_strand,on_delete=models.CASCADE,null=True)
    date = models.DateField(timezone.now())

class AuthenticAssessment(models.Model):
    teacher = models.ForeignKey(User,on_delete=models.CASCADE)
    grade = models.CharField(choices=grade,max_length=1100)
    learning_area = models.ForeignKey(LearningArea,on_delete=models.CASCADE,null=True)
    strand = models.ForeignKey(Strand,on_delete=models.CASCADE,null=True)
    sub_strand = models.ForeignKey(Sub_strand,on_delete=models.CASCADE,null=True)
    date = models.DateField(timezone.now())
    task = models.CharField(max_length=200)
    max_score = models.IntegerField()
    
class WrittenTest(models.Model):
    teacher = models.ForeignKey(User,on_delete=models.CASCADE)
    grade = models.CharField(choices=grade,max_length=100)
    learning_area = models.ForeignKey(LearningArea,on_delete=models.CASCADE,null=True)
    strand = models.ForeignKey(Strand,on_delete=models.CASCADE,null=True)   
    date = models.DateField(timezone.now())
    max_score = models.IntegerField()
    
class SummativeAssessment(models.Model):
    grade = models.CharField(choices=grade,max_length=100)
    term = models.CharField(choices=term,max_length=100)
    year = models.CharField(choices=year,max_length=10000)
    type = models.ForeignKey(SummativeType,on_delete=models.CASCADE,null=True)
    learning_area = models.ForeignKey(LearningArea,on_delete=models.CASCADE,null=True)
    date = models.DateField(timezone.now())
    max_score = models.IntegerField()
    
class Portfolio(models.Model):
    grade = models.CharField(choices=grade,max_length=100)
    term = models.CharField(choices=term,max_length=100)
    year = models.CharField(choices=year,max_length=10000)
    learning_area = models.ForeignKey(LearningArea,on_delete=models.CASCADE,null=True)
    learner = models.ForeignKey(Strand,on_delete=models.CASCADE,null=True)
    portfolio = models.FileField(upload_to='media/portfolios')