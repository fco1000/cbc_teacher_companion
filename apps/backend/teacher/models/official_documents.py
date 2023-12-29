from django.db import models
from django.utils import timezone
from teacher.models import User
from school_info.models import Strand,Sub_strand

'''
Professional documents
Schemes of work
Lesson plan
record of work
'''

class SchemesOfWork(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    # Admin details
    strand = models.ForeignKey(Strand,on_delete=models.CASCADE)
    sub_strand = models.ForeignKey(Sub_strand,on_delete=models.CASCADE)
    lesson = models.CharField(max_length=100)
    specific_learning_outcomes = models.TextField(max_length=500)
    learning_experiences = models.TextField(max_length=500)
    key_inquiry_question = models.TextField(max_length=500)
    resources = models.TextField(max_length=100)
    # 
    assesment = models.CharField(max_length=200)
    reflection = models.TextField(max_length=200)
    
    def __str__(self):
        return self.lesson
    

class LessonPlan(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    # Admin details
    strand = models.ForeignKey(Strand,on_delete=models.CASCADE)
    sub_strand = models.ForeignKey(Sub_strand,on_delete=models.CASCADE)
    lesson = models.ForeignKey(SchemesOfWork,on_delete=models.CASCADE)
    specific_learning_outcomes = models.TextField(max_length=500)
    learning_experiences = models.TextField(max_length=500)
    key_inquiry_question = models.TextField(max_length=500)
    resources = models.TextField(max_length=100)
    # Lesson development
    steps = models.TextField(max_length=1000)
    extended_activity = models.TextField(max_length=500)
    conclusion = models.TextField(max_length=250)
    
    def __str__(self):
        return self.lesson

class RecordOfWord(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    lesson = models.OneToOneField(LessonPlan,on_delete=models.CASCADE)
    workdone = models.TextField(max_length=500)
    reflection = models.TextField(max_length=500)
    
    def __str__(self):
        return f'{self.teacher}: {self.lesson} - {self.date}' 
    