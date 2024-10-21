from django.urls import path
from .views import ProjectView,Project_typesView


urlpatterns = [
    path('project_create/',ProjectView.as_view(),name='project'),
    path('type_create/',Project_typesView.as_view(),name='type_create')


    
]