from django.db import models
from PIL import Image

grade = [
    ('PP1','PP 1'),
    ('PP2','PP 2'),
    ('Grade1','Grade 1'),
    ('Grade2','Grade 2'),
    ('Grade3','Grade 3'),
    ('Grade4','Grade 4'),
    ('Grade5','Grade 5'),
    ('Grade6','Grade 6'),
    ('Grade7','Grade 7'),
    ('Grade8','Grade 8'),
    ('Grade9','Grade 9'),
]

term = [
    ('Term1','1'),
    ('Term2','2'),
    ('Term3','3')
]
    
year = [
    ('2023','2023'),
]

remark = [
    ('Above Expectations','Above Expectations'),
    ('Meets Expectations','Meets Expectations'),
    ('Approaching Expectations','Approaching Expectations'),
    ('Below Expectations','Below Expectations'),
    
    
    
]    

class LearningArea(models.Model):
    grade = models.CharField(choices=grade,max_length=101)
    learningArea = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.learningArea}'
    
class SummativeType(models.Model):
    type = models.CharField(max_length=100)
    
    def __str__(self):
        return self.type
    
class TermDates(models.Model):
    event = models.CharField(max_length=100)
    date = models.DateField()
    
    def __str__(self):
        return f'{self.event} - {self.date}'

class Learner(models.Model):
    admissionNo = models.IntegerField(primary_key=True,null=False,unique=True)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    home_address = models.CharField(max_length=100)
    parent_or_guardian = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    year_joined = models.DateField()
    picture = models.ImageField(upload_to='media/leaners',default='media/default.png',null=True)
    
    def __str__(self):
        return f'{self.admissionNo} - {self.name}'
    
    def save(self, *args, **kwargs):
        super().save()
        
        img = Image.open(self.picture.path)
        
        if img.height > 900 or img.width > 900:
            outputsize = (900, 900)
            img.thumbnail(outputsize)
            img.save(self.picture.path)