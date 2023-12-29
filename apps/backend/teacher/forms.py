from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import (
    User,
    LessonPlan,
    Position,
    RecordOfWord,
    SchemesOfWork
    )

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'email',
            'tscNo',
            'phoneNo',
            'learningAreas',
            'position',
            'profile_photo',
        ]
        labels = [
            'Email',
            'TSC No.',
            'Phone No.',
            'Learning Areas',
            'Profile Photo',
        ]
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'email',
            'tscNo',
            'phoneNo',
            'learningAreas',
            'position',
            'profile_photo',
        ]
        labels = [
            'Email',
            'TSC No.',
            'Phone No.',
            'Learning Areas',
            'Profile Photo',
        ]
        
class LessonPlanForm(forms.ModelForm):
    class Meta:
        model = LessonPlan
        fields = '__all__'
        
        
class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = '__all__'
        
        
class RecordOfWordForm(forms.ModelForm):
    class Meta:
        model = RecordOfWord
        fields = '__all__'
        
        
class SchemesOfWorkForm(forms.ModelForm):
    class Meta:
        model = SchemesOfWork
        fields = '__all__'
        
