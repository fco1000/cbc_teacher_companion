from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.utils.translation import gettext_lazy as _
from teacher.managers import CustomUserManager

from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException

from django.core.exceptions import ValidationError

# Create your models here.
class Position(models.Model):
    position = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.position}'
    
class User(AbstractUser):
    username = None
    email = models.EmailField(_("Email address"), unique=True)
    tscNo = models.BigIntegerField(unique=True,null=True, blank=True)
    phoneNo = models.BigIntegerField(null = True,blank=True)
    school = models.ForeignKey('School',on_delete=models.CASCADE,null=True)
    learningAreas = models.ManyToManyField('school_info.LearningArea',blank=True)
    position = models.ForeignKey(Position,on_delete=models.CASCADE,null=True)
    profile_photo = models.ImageField(upload_to='media/profiles',default='media/default.png',null=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super(User, self).save(*args, **kwargs)
        
        img = Image.open(self.profile_photo.path)
            
        if img.height > 900 or img.width > 900:
                outputsize = (900, 900)
                img.thumbnail(outputsize)
                img.save(self.profile_photo.path)
                
    def clean(self):
        if self.position == "Headteacher":
            if User.objects.filter(school=self.school, position = 'Headteacher').count() > 0:
                raise DuplicateHeadteacherError("A school can only have one Headteacher")
        elif self.position == "Deputy headteacher":
            if User.objects.filter(school=self.school, position = 'Deputy headteacher').count() <= 5:
                raise ExcessDeputyHeadteacherError("A school should have at most 5 Deputy headteachers")    
    

                
class School(models.Model):
    school_name = models.CharField(max_length=300)
    head_name = models.CharField(max_length=120,null = True)
    
    def __str__(self):
        return f'{self.school_name}'
    
    
class DuplicateHeadteacherError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'A school can only have one headteacher'

class ExcessDeputyHeadteacherError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'A school cannot have more than five deputy headteachers'