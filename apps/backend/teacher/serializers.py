from rest_framework import serializers
from .models import (
    User,
    LessonPlan,
    Position,
    RecordOfWord,
    SchemesOfWork,
    School
)

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','first_name','last_name','email','school','tscNo','phoneNo','learningAreas','position','profile_photo']
            
class LessonPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonPlan
        fields = ['teacher','strand','sub_strand','lesson','specific_learning_outcomes','learning_experiences','key_inquiry_question','resources','steps','extended_activity','conclusion']
        
class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'
        
class RecordOfWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordOfWord
        fields = '__all__'
        
class SchemesOfWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchemesOfWork
        fields = '__all__'

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'