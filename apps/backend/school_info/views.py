from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import viewsets     
from rest_framework.generics import ListAPIView
from .serializers import (
    LearnerSerializer,
    LearningAreaSerializer,
    StrandSerializer,
    Sub_strandSerializer,
    AuthenticAssessmentRubricSerializer,
    AuthenticAssessmentSerializer,
    ClassActivitieSerializer,
    PortfolioSerializer,
    ProjectRubricSerializer,
    SummativeAssessmentSerializer,
    WrittenTestSerializer 
)

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

# Create your views here.
class LearnerView(viewsets.ModelViewSet):
    serializer_class = LearnerSerializer
    
    def get_queryset(self):
        Learners = Learner.objects.all()
        return Learners
    
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        # params_list = params["pk"].split('-')
        Learners = Learner.objects.filter(admissionNo =params['pk'])
        serializer = LearnerSerializer(Learners, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        Learner_data = request.data
        new_Learner = Learner.objects.create(
            admissionNo=Learner_data['admissionNo'],
            name=Learner_data['name'],
            date_of_birth=Learner_data['date_of_birth'],
            home_address=Learner_data['home_address'],
            parent_or_guardian=Learner_data['parent_or_guardian'],
            phone_number=Learner_data['phone_number'],
            year_joined=Learner_data['year_joined']            ,
        )
        new_Learner.save()
        
        serializer = LearnerSerializer(new_Learner)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        loged_in_user = request.user
        if loged_in_user == "admin":
            Learner = self.get_object()
            Learner.delete()
            responseMessage = {"message":"Object has been deleted"}
        else:
            responseMessage = {"message":"you are not allowed"}
        
        return Response(responseMessage)
    
class LearningAreaView(viewsets.ModelViewSet):
    serializer_class = LearningAreaSerializer
    
    def get_queryset(self):
        LearningAreas = LearningArea.objects.all()
        return LearningAreas
    
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        # params_list = params["pk"].split('-')
        LearningAreas = LearningArea.objects.filter(id=params['pk'])
        serializer = LearningAreaSerializer(LearningAreas, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        LearningArea_data = request.data
        new_LearningArea = LearningArea.objects.create(
            grade=LearningArea_data['grade'],
            learningArea=LearningArea_data['learningArea'],
        )
        new_LearningArea.save()
        
        serializer = LearningAreaSerializer(new_LearningArea)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        loged_in_user = request.user
        if loged_in_user == "admin":
            LearningArea = self.get_object()
            LearningArea.delete()
            responseMessage = {"message":"Object has been deleted"}
        else:
            responseMessage = {"message":"you are not allowed"}
        
        return Response(responseMessage)
    
class StrandView(viewsets.ModelViewSet):
    serializer_class = StrandSerializer
    
    def get_queryset(self):
        Strands = Strand.objects.all()
        return Strands
    
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        # params_list = params["pk"].split('-')
        Strands = Strand.objects.filter(id =params['pk'])
        serializer = StrandSerializer(Strands, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        Strand_data = request.data
        new_Strand = Strand.objects.create(
            learningArea=Strand_data['learningArea'],
            strand=Strand_data['strand'],
        )
        new_Strand.save()
        
        serializer = StrandSerializer(new_Strand)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        loged_in_user = request.user
        if loged_in_user == "admin":
            Strand = self.get_object()
            Strand.delete()
            responseMessage = {"message":"Object has been deleted"}
        else:
            responseMessage = {"message":"you are not allowed"}
        
        return Response(responseMessage)
    
class Sub_strandView(viewsets.ModelViewSet):
    serializer_class = Sub_strandSerializer
    
    def get_queryset(self):
        Sub_strands = Sub_strand.objects.all()
        return Sub_strands
    
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        # params_list = params["pk"].split('-')
        Sub_strands = Sub_strand.objects.filter(id =params['pk'])
        serializer = Sub_strandSerializer(Sub_strands, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        Sub_strand_data = request.data
        new_Sub_strand = Sub_strand.objects.create(
            strand=Sub_strand_data['strand'],
            subStrand=Sub_strand_data['subStrand'],
        )
        new_Sub_strand.save()
        
        serializer = Sub_strandSerializer(new_Sub_strand)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        loged_in_user = request.user
        if loged_in_user == "admin":
            Sub_strand = self.get_object()
            Sub_strand.delete()
            responseMessage = {"message":"Object has been deleted"}
        else:
            responseMessage = {"message":"you are not allowed"}
        
        return Response(responseMessage)
    
class AuthenticAssessmentRubricView(viewsets.ModelViewSet):
    serializer_class = AuthenticAssessmentRubricSerializer
    
    def get_queryset(self):
        AuthenticAssessmentRubrics = AuthenticAssessmentRubric.objects.all()
        return AuthenticAssessmentRubrics
    
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        # params_list = params["pk"].split('-')
        AuthenticAssessmentRubrics = AuthenticAssessmentRubric.objects.filter(id =params['pk'])
        serializer = AuthenticAssessmentRubricSerializer(AuthenticAssessmentRubrics, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        AuthenticAssessmentRubric_data = request.data
        new_AuthenticAssessmentRubric = AuthenticAssessmentRubric.objects.create(
            term = AuthenticAssessmentRubric_data['term'],
            year = AuthenticAssessmentRubric_data['year'],
            learning_area = AuthenticAssessmentRubric_data['learning_area'],
            strand = AuthenticAssessmentRubric_data['strand'],
            task = AuthenticAssessmentRubric_data['task'],
            date = AuthenticAssessmentRubric_data['date'],
            criteria = AuthenticAssessmentRubric_data['criteria'],
            exceeds_expectations = AuthenticAssessmentRubric_data['exceeds_expectations'],
            meets_expectations = AuthenticAssessmentRubric_data['meets_expectations'],
            approaches_expectations = AuthenticAssessmentRubric_data['approaches_expectations'],
            below_expectations = AuthenticAssessmentRubric_data['below_expectations']
        )
        new_AuthenticAssessmentRubric.save()
        
        serializer = AuthenticAssessmentRubricSerializer(new_AuthenticAssessmentRubric)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        loged_in_user = request.user
        if loged_in_user == "admin":
            AuthenticAssessmentRubric = self.get_object()
            AuthenticAssessmentRubric.delete()
            responseMessage = {"message":"Object has been deleted"}
        else:
            responseMessage = {"message":"you are not allowed"}
        
        return Response(responseMessage)
    
class AuthenticAssessmentView(viewsets.ModelViewSet):
    serializer_class = AuthenticAssessmentSerializer
    
    def get_queryset(self):
        AuthenticAssessments = AuthenticAssessment.objects.all()
        return AuthenticAssessments
    
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        # params_list = params["pk"].split('-')
        AuthenticAssessments = AuthenticAssessment.objects.filter(id =params['pk'])
        serializer = AuthenticAssessmentSerializer(AuthenticAssessments, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        AuthenticAssessment_data = request.data
        new_AuthenticAssessment = AuthenticAssessment.objects.create(
            teacher = AuthenticAssessment_data['teacher'],
            grade = AuthenticAssessment_data['grade'],
            learning_area = AuthenticAssessment_data['learning_area'],
            strand = AuthenticAssessment_data['strand'],
            sub_strand = AuthenticAssessment_data['sub_strand'],
            date = AuthenticAssessment_data['date'],
            task = AuthenticAssessment_data['task'],
            max_score = AuthenticAssessment_data['max_score'],
            score = AuthenticAssessment_data['score'],
            remark = AuthenticAssessment_data['remark'],
        )
        new_AuthenticAssessment.save()
        
        serializer = AuthenticAssessmentSerializer(new_AuthenticAssessment)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        loged_in_user = request.user
        if loged_in_user == "admin":
            AuthenticAssessment = self.get_object()
            AuthenticAssessment.delete()
            responseMessage = {"message":"Object has been deleted"}
        else:
            responseMessage = {"message":"you are not allowed"}
        
        return Response(responseMessage)
    
class ClassActivitieView(viewsets.ModelViewSet):
    serializer_class = ClassActivitieSerializer
    
    def get_queryset(self):
        ClassActivities = ClassActivitie.objects.all()
        return ClassActivities
    
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        # params_list = params["pk"].split('-')
        ClassActivities = ClassActivitie.objects.filter(id =params['pk'])
        serializer = ClassActivitieSerializer(ClassActivities, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        ClassActivitie_data = request.data
        new_ClassActivitie = ClassActivitie.objects.create(
            grade = ClassActivitie_data['grade'],
            learning_area = ClassActivitie_data['learning_area'],
            strand = ClassActivitie_data['strand'],
            sub_strand = ClassActivitie_data['sub_strand'],
            date = ClassActivitie_data['date'],
        )
        new_ClassActivitie.save()
        
        serializer = ClassActivitieSerializer(new_ClassActivitie)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        loged_in_user = request.user
        if loged_in_user == "admin":
            ClassActivitie = self.get_object()
            ClassActivitie.delete()
            responseMessage = {"message":"Object has been deleted"}
        else:
            responseMessage = {"message":"you are not allowed"}
        
        return Response(responseMessage)
    
class PortfolioView(viewsets.ModelViewSet):
    serializer_class = PortfolioSerializer
    
    def get_queryset(self):
        Portfolios = Portfolio.objects.all()
        return Portfolios
    
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        # params_list = params["pk"].split('-')
        Portfolios = Portfolio.objects.filter(id =params['pk'])
        serializer = PortfolioSerializer(Portfolios, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        Portfolio_data = request.data
        new_Portfolio = Portfolio.objects.create(
            grade = Portfolio_data['grade'],
            term = Portfolio_data['term'],
            year = Portfolio_data['year'],
            learning_area = Portfolio_data['learning_area'],
            learner = Portfolio_data['learner'],
            portfolio = Portfolio_data['portfolio'],
        )
        new_Portfolio.save()
        
        serializer = PortfolioSerializer(new_Portfolio)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        loged_in_user = request.user
        if loged_in_user == "admin":
            Portfolio = self.get_object()
            Portfolio.delete()
            responseMessage = {"message":"Object has been deleted"}
        else:
            responseMessage = {"message":"you are not allowed"}
        
        return Response(responseMessage)
    
class ProjectRubricView(viewsets.ModelViewSet):
    serializer_class = ProjectRubricSerializer
    
    def get_queryset(self):
        ProjectRubrics = ProjectRubric.objects.all()
        return ProjectRubrics
    
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        # params_list = params["pk"].split('-')
        ProjectRubrics = ProjectRubric.objects.filter(id =params['pk'])
        serializer = ProjectRubricSerializer(ProjectRubrics, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        ProjectRubric_data = request.data
        new_ProjectRubric = ProjectRubric.objects.create(
            term = ProjectRubric_data['term'],
            year = ProjectRubric_data['year'],
            learning_area = ProjectRubric_data['learning_area'],
            strand = ProjectRubric_data['strand'],
            skills_tested = ProjectRubric_data['skills_tested'],
            values_to_be_learned = ProjectRubric_data['values_to_be_learned'],
        )
        new_ProjectRubric.save()
        
        serializer = ProjectRubricSerializer(new_ProjectRubric)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        loged_in_user = request.user
        if loged_in_user == "admin":
            ProjectRubric = self.get_object()
            ProjectRubric.delete()
            responseMessage = {"message":"Object has been deleted"}
        else:
            responseMessage = {"message":"you are not allowed"}
        
        return Response(responseMessage)
    
class SummativeAssessmentView(viewsets.ModelViewSet):
    serializer_class = SummativeAssessmentSerializer
    
    def get_queryset(self):
        SummativeAssessments = SummativeAssessment.objects.all()
        return SummativeAssessments
    
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        # params_list = params["pk"].split('-')
        SummativeAssessments = SummativeAssessment.objects.filter(id =params['pk'])
        serializer = SummativeAssessmentSerializer(SummativeAssessments, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        SummativeAssessment_data = request.data
        new_SummativeAssessment = SummativeAssessment.objects.create(
            grade = SummativeAssessment_data['grade'],
            term = SummativeAssessment_data['term'],
            year = SummativeAssessment_data['year'],
            type = SummativeAssessment_data['type'],
            learning_area = SummativeAssessment_data['learning_area'],
            date = SummativeAssessment_data['date'],
            max_score = SummativeAssessment_data['max_score'],
            score = SummativeAssessment_data['score'],
            remark = SummativeAssessment_data['remark'],
            classteacher_remark = SummativeAssessment_data['classteacher_remark'],
            headteacher_remark = SummativeAssessment_data['headteacher_remark'],
        )
        new_SummativeAssessment.save()
        
        serializer = SummativeAssessmentSerializer(new_SummativeAssessment)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        loged_in_user = request.user
        if loged_in_user == "admin":
            SummativeAssessment = self.get_object()
            SummativeAssessment.delete()
            responseMessage = {"message":"Object has been deleted"}
        else:
            responseMessage = {"message":"you are not allowed"}
        
        return Response(responseMessage)
    
class WrittenTestView(viewsets.ModelViewSet):
    serializer_class = WrittenTestSerializer
    
    def get_queryset(self):
        WrittenTests = WrittenTest.objects.all()
        return WrittenTests
    
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        # params_list = params["pk"].split('-')
        WrittenTests = WrittenTest.objects.filter(id =params['pk'])
        serializer = WrittenTestSerializer(WrittenTests, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        WrittenTest_data = request.data
        teacher = request.user
        new_WrittenTest = WrittenTest.objects.create(
            teacher = teacher,
            grade = WrittenTest_data['grade'],
            learning_area = WrittenTest_data['learning_area'],
            strand = WrittenTest_data['strand'],
            date = WrittenTest_data['date'],
            max_score = WrittenTest_data['max_score'],
            score = WrittenTest_data['score'],
            remark = WrittenTest_data['remark'],
        )
        new_WrittenTest.save()
        
        serializer = WrittenTestSerializer(new_WrittenTest)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        loged_in_user = request.user
        if loged_in_user == "admin":
            WrittenTest = self.get_object()
            WrittenTest.delete()
            responseMessage = {"message":"Object has been deleted"}
        else:
            responseMessage = {"message":"you are not allowed"}
        
        return Response(responseMessage)
    
    
    
    
    
    
    