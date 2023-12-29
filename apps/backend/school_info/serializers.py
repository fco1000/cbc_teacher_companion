from rest_framework import serializers
from .models import (
    Learner,
    LearningArea,
    Strand,
    Sub_strand,
    AuthenticAssessmentRubric,
    AuthenticAssessment,
    ClassActivitie,
    Portfolio,
    ProjectRubric,
    SummativeAssessment,
    WrittenTest 
)

class LearnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Learner
        fields = ['admissionNo','name','date_of_birth','home_address','parent_or_guardian','phone_number','year_joined']

class LearningAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningArea
        fields = '__all__'

class StrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Strand
        fields = '__all__'

class Sub_strandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_strand
        fields = '__all__'

class AuthenticAssessmentRubricSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthenticAssessmentRubric
        fields = '__all__'

class AuthenticAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthenticAssessment
        fields = '__all__'

class ClassActivitieSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassActivitie
        fields = '__all__'

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'

class ProjectRubricSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectRubric
        fields = '__all__'

class SummativeAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SummativeAssessment
        fields = '__all__'

class WrittenTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WrittenTest
        fields = '__all__'
