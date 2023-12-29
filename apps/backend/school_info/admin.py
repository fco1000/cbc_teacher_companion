from django.contrib import admin
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
# Register your models here.
admin.site.register(Learner)
admin.site.register(LearningArea)
admin.site.register(Strand)
admin.site.register(Sub_strand)
admin.site.register(AuthenticAssessmentRubric)
admin.site.register(AuthenticAssessment)
admin.site.register(ClassActivitie)
admin.site.register(Portfolio)
admin.site.register(ProjectRubric)
admin.site.register(SummativeAssessment)
admin.site.register(WrittenTest)