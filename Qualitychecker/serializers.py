from rest_framework import serializers
from .models import Project,Quality_check,Qualitycheck_Output,Team,Annotaor,Project_types

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields='__all__'

class Project_typesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project_types
        fields='__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=Team
        fields='__all__'

class AnnotatorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Annotaor
        fields='__all__'

class QualitycheckSerializer(serializers.ModelSerializer):
    class Meta:
        model=Quality_check
        fields='__all__'

class QualitycheckoutputSerializer(serializers.ModelSerializer):
    class Meta:
        model=Qualitycheck_Output
        fields='__all__'
    
    