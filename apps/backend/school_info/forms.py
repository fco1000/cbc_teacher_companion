from .models import (
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
from django import forms

class LearnerAdmissionForm(forms.ModelForm):
    class Meta:
        model = LearningArea
        fields = [
            'admissionNo',
            'name',
            'date_of_birth',
            'home_address',
            'parent_or_guardian',
            'phone_number',
            'year_joined',
        ]
        labels = [
            'Admission No.',
            'Name',
            'Date of Birth',
            'Address',
            'Parent/Guardian',
            'Phone Number',
            'Year Admitted',
        ]
        
class StrandForm(forms.ModelForm):
    class Meta:
        model = Strand
        fields = '__all__'
        
class Sub_strandForm(forms.ModelForm):
    class Meta:
        model = Sub_strand
        fields = '__all__'
        
class AuthenticAssessmentRubricForm(forms.ModelForm):
    class Meta:
        model = AuthenticAssessmentRubric
        fields = '__all__'
        
class AuthenticAssessmentForm(forms.ModelForm):
    class Meta:
        model = AuthenticAssessment
        fields = '__all__'
        
class ClassActivitieForm(forms.ModelForm):
    class Meta:
        model = ClassActivitie
        fields = '__all__'
        
class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = '__all__'
        
class ProjectRubricForm(forms.ModelForm):
    class Meta:
        model = ProjectRubric
        fields = '__all__'
        
class SummativeAssessmentForm(forms.ModelForm):
    class Meta:
        model = SummativeAssessment
        fields = '__all__'
        
class WrittenTestForm(forms.ModelForm):
    class Meta:
        model = WrittenTest
        fields = '__all__'
  