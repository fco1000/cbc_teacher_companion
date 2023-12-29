from django.urls import path,include
from .views import (
    LearnerView,
    LearningAreaView,
    StrandView,
    Sub_strandView,
    AuthenticAssessmentRubricView,
    AuthenticAssessmentView,
    ClassActivitieView,
    PortfolioView,
    ProjectRubricView,
    SummativeAssessmentView,
    WrittenTestView,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('learners',LearnerView,basename='learners')
router.register('LearningArea',LearningAreaView,basename='LearningArea')
router.register('Strand',StrandView,basename='Strand')
router.register('Sub_strand',Sub_strandView,basename='Sub_strand')
router.register('AuthenticAssessmentRubric',AuthenticAssessmentRubricView,basename='AuthenticAssessmentRubric')
router.register('AuthenticAssessment',AuthenticAssessmentView,basename='AuthenticAssessment')
router.register('ClassActivitie',ClassActivitieView,basename='ClassActivitie')
router.register('Portfolio',PortfolioView,basename='Portfolio')
router.register('ProjectRubric',ProjectRubricView,basename='ProjectRubric')
router.register('SummativeAssessment',SummativeAssessmentView,basename='SummativeAssessment')
router.register('WrittenTest',WrittenTestView,basename='WrittenTest')

urlpatterns = [
    path('',include(router.urls)),
]