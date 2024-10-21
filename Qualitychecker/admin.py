from django.contrib import admin
from .models import Project,Team,Quality_check,Qualitycheck_Output,Annotaor,Project_types
# Register your models here.
admin.site.register(Project)
admin.site.register(Team)
admin.site.register(Quality_check)
admin.site.register(Qualitycheck_Output)
admin.site.register(Annotaor)
admin.site.register(Project_types)