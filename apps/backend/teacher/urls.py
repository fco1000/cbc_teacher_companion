from django.urls import path,include
from .views import (
    PositionView,
    LessonPlanView,
    RecordOfWordView,
    UserView,
    SchemesOfWorkView,
    SchoolView
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('position',PositionView,basename='position')
router.register('LessonPlan',LessonPlanView,basename='LessonPlan')
router.register('RecordOfWord',RecordOfWordView,basename='RecordOfWord')
router.register('User',UserView,basename='User')
router.register('SchemesOfWork',SchemesOfWorkView,basename='SchemesOfWork')
router.register('School',SchoolView,basename='School')

urlpatterns = [
    path('',include(router.urls))
]