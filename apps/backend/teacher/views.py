from django.shortcuts import render
from django.contrib.auth.hashers import make_password

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets, status
from django.core.mail import send_mail
import secrets
from rest_framework.generics import ListAPIView
from .models import (
    LessonPlan,
    Position,
    RecordOfWord, 
    SchemesOfWork, 
    User, 
    School,
    DuplicateHeadteacherError,
    ExcessDeputyHeadteacherError
    )
from .serializers import (
    CustomUserSerializer,
    LessonPlanSerializer,
    PositionSerializer,
    RecordOfWordSerializer,
    SchemesOfWorkSerializer,
    SchoolSerializer,
)
from school_info.models import LearningArea

from teacher.helper import (
    is_headmaster_or_deputy,
    is_admin,
    send_account_email,
    generate_random_password,
)


# Create your views here.
# random password generator


class UserView(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        Users = User.objects.all()
        return Users

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        # params_list = params["pk"].split('-')
        Users = User.objects.filter(id=params["pk"])
        serializer = CustomUserSerializer(Users, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        User_data = request.data
        # Check if the user creating the account is the headmaster or deputy
        if not is_headmaster_or_deputy(request.user) or not is_admin(request.user):
            # generates random password for the user
            try:
                password = generate_random_password()
                new_User = User.objects.create(
                    email=User_data["email"],
                    password=make_password(password),
                    position=Position.objects.get(id = User_data["position"]),
                    school=School.objects.get(school_name = request.user.school),
                )
                # tries to send the email with the user's login details
                try:
                    send_account_email(new_User.email, password)
                except:
                    return Response(
                        {
                            "message": "Could not send the email. But the password is: "
                            + password
                            + ". Please note it down somewhere for safekeeping as you will not have a chance to view it again"
                        }
                    )

                # Serialize the user object
                serializer = CustomUserSerializer(new_User)
                serializer(raise_exception=True)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except DuplicateHeadteacherError as e:
                return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)
            except ExcessDeputyHeadteacherError as e:
                return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {
                    "message": "You are not allowed to create users. This action is reserved for admins only"
                },
                status=status.HTTP_403_FORBIDDEN,
            )
    
    def destroy(self, request, *args, **kwargs):
        logged_in_user = request.user.groups
        if logged_in_user == "admin" or "headmaster":
            User = self.get_object()
            User.delete()
            responseMessage = {"message": "Object has been deleted"}
        else:
            responseMessage = {"message": "you are not allowed"}

        return Response(responseMessage)


class LessonPlanView(viewsets.ModelViewSet):
    serializer_class = LessonPlanSerializer

    def get_queryset(self):
        LessonPlans = LessonPlan.objects.all()
        return LessonPlans

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        # params_list = params["pk"].split('-')
        LessonPlans = LessonPlan.objects.filter(id=params["pk"])
        serializer = LessonPlanSerializer(LessonPlans, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        LessonPlan_data = request.data
        teacher = request.user
        new_LessonPlan = LessonPlan.objects.create(
            teacher=teacher,
            grade=LessonPlan_data["grade"],
            learning_area=LessonPlan_data["learning_area"],
            strand=LessonPlan_data["strand"],
            date=LessonPlan_data["date"],
            max_score=LessonPlan_data["max_score"],
            score=LessonPlan_data["score"],
            remark=LessonPlan_data["remark"],
        )
        new_LessonPlan.save()

        serializer = LessonPlanSerializer(new_LessonPlan)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        loged_in_user = request.user
        if loged_in_user == "admin":
            LessonPlan = self.get_object()
            LessonPlan.delete()
            responseMessage = {"message": "Object has been deleted"}
        else:
            responseMessage = {"message": "you are not allowed"}

        return Response(responseMessage)


class PositionView(viewsets.ModelViewSet):
    serializer_class = PositionSerializer

    def get_queryset(self):
        Positions = Position.objects.all()
        return Positions

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        # params_list = params["pk"].split('-')
        Positions = Position.objects.filter(id=params["pk"])
        serializer = PositionSerializer(Positions, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        Position_data = request.data
        new_Position = Position.objects.create(
            position=Position_data["position"],
        )
        new_Position.save()

        serializer = PositionSerializer(new_Position)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        loged_in_user = request.user
        if loged_in_user == "admin":
            Position = self.get_object()
            Position.delete()
            responseMessage = {"message": "Object has been deleted"}
        else:
            responseMessage = {"message": "you are not allowed"}

        return Response(responseMessage)


class RecordOfWordView(viewsets.ModelViewSet):
    serializer_class = RecordOfWordSerializer

    def get_queryset(self):
        RecordOfWords = RecordOfWord.objects.all()
        return RecordOfWords

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        # params_list = params["pk"].split('-')
        RecordOfWords = RecordOfWord.objects.filter(id=params["pk"])
        serializer = RecordOfWordSerializer(RecordOfWords, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        RecordOfWord_data = request.data
        teacher = request.user
        new_RecordOfWord = RecordOfWord.objects.create(
            teacher=teacher,
            date=RecordOfWord_data["date"],
            lesson=RecordOfWord_data["lesson"],
            workdone=RecordOfWord_data["workdone"],
            reflection=RecordOfWord_data["reflection"],
        )
        new_RecordOfWord.save()

        serializer = RecordOfWordSerializer(new_RecordOfWord)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        loged_in_user = request.user
        if loged_in_user == "admin":
            RecordOfWord = self.get_object()
            RecordOfWord.delete()
            responseMessage = {"message": "Object has been deleted"}
        else:
            responseMessage = {"message": "you are not allowed"}

        return Response(responseMessage)


class SchemesOfWorkView(viewsets.ModelViewSet):
    serializer_class = SchemesOfWorkSerializer

    def get_queryset(self):
        SchemesOfWorks = SchemesOfWork.objects.all()
        return SchemesOfWorks

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        # params_list = params["pk"].split('-')
        SchemesOfWorks = SchemesOfWork.objects.filter(id=params["pk"])
        serializer = SchemesOfWorkSerializer(SchemesOfWorks, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        SchemesOfWork_data = request.data
        teacher = request.user
        new_SchemesOfWork = SchemesOfWork.objects.create(
            teacher=teacher,
            strand=SchemesOfWork_data["strand"],
            sub_strand=SchemesOfWork_data["sub_strand"],
            lesson=SchemesOfWork_data["lesson"],
            specific_learning_outcomes=SchemesOfWork_data["specific_learning_outcomes"],
            learning_experiences=SchemesOfWork_data["learning_experiences"],
            key_inquiry_question=SchemesOfWork_data["key_inquiry_question"],
            resources=SchemesOfWork_data["resources"],
            assesment=SchemesOfWork_data["assesment"],
            reflection=SchemesOfWork_data["reflection"],
        )
        new_SchemesOfWork.save()

        serializer = SchemesOfWorkSerializer(new_SchemesOfWork)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        loged_in_user = request.user
        if loged_in_user == "admin":
            SchemesOfWork = self.get_object()
            SchemesOfWork.delete()
            responseMessage = {"message": "Object has been deleted"}
        else:
            responseMessage = {"message": "you are not allowed"}

        return Response(responseMessage)


class SchoolView(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer

    def get_queryset(self):
        Schools = School.objects.all()
        return Schools

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        # params_list = params["pk"].split('-')
        Schools = School.objects.filter(id=params["pk"])
        serializer = SchoolSerializer(Schools, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        School_data = request.data
        teacher = request.user
        new_School = School.objects.create(
            school_name=School_data["school_name"],
            head_name=School_data["head_name"],
        )
        new_School.save()

        serializer = SchoolSerializer(new_School)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        loged_in_user = request.user
        if loged_in_user == "admin":
            School = self.get_object()
            School.delete()
            responseMessage = {"message": "Object has been deleted"}
        else:
            responseMessage = {"message": "you are not allowed"}

        return Response(responseMessage)
