from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Project
from .serializers import ProjectSerializer,Project_typesSerializer,TeamSerializer,AnnotatorSerializer,QualitycheckSerializer,QualitycheckoutputSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated


class ProjectView(APIView):
    def post(self, request, format=None):
        serializer = ProjectSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            project_id = serializer.validated_data.get('project_Id')  # Adjust to your field name
            project_name = serializer.validated_data.get('project_name')  # Use the correct field name

            # Check if a project ID already exists
            existing_project = Project.objects.filter(project_Id=project_id).first()

            if existing_project:
                return Response({'msg': f'A project with ID {project_id} already exists.'}, status=status.HTTP_400_BAD_REQUEST)

            # Check if a project name already exists
            existing_project_by_name = Project.objects.filter(project_name=project_name).first()
            if existing_project_by_name:
                return Response({'msg': f'A project with the name "{project_name}" already exists.'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({'msg': 'Project created successfully.'}, status=status.HTTP_201_CREATED)
        

class Project_typesView(APIView):
    def post(self, request, format=None):
        serializer = Project_typesSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg': 'Project created successfully.'}, status=status.HTTP_201_CREATED)
        

class TeamCreateView(APIView):
    def post(self, request, format=None):
        serializer=TeamSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Team created sucessfully'},status=status.HTTP_201_CREATED)
