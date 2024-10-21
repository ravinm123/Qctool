from django.db import models
from Quality.models import User




# def laod_Role():
#     current_dir=os .path.dirname(os.path.abspath(__file__))
#     file_name='role_choices.json'
#     file_path=os.path.json(current_dir,file_name)

#     with open(file_path,'r') as file:
#         role_choices=json.load(file)
#     return role_choices

class Project(models.Model):
#     PROJECT_CHOICES = [
#     ('Project_Eagle', 'Project Eagle'),
#     ('Project_Original', 'Project Original'),
#     ('Project_Dspace', 'Project Dspace'),
# ]



    project_name=models.CharField(max_length=250,)
    project_Id=models.IntegerField()
    def __str__(self):
        return self.project_name


class Project_types(models.Model):
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)  
    # TASK_TYPE=[
    #     ('2d bb creation','2D BB Creation'),
    #     ('3d bb creation', '3D BB Creation'),
    #     ('2d bb check and correct','2D BB Check and Correct'),
    #     ('3dbb/2d bb deletion','3DBB/2D BB Deletion'),
    #     ('2d polyline','2D Polyline'),
    #     ('3d/2d bb dynamic','3D/2D BB DYNAMIC'),
    #     ('3d/2d bb static','3D/2D BB STATIC')

    # ] 

    task_type = models.CharField(max_length=250)


    

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    Team_choice=[
        ('Team_Pioneers','UAI Team'),
        ('Team_Pixel','UAI Team'),
        ('Team_Alpha','Magna Team'),
        ('Team_Phoenix','Up2datz')
    ]
    team_name=models.CharField(max_length=250,choices=Team_choice)
    lead_name=models.CharField(max_length=50,default='other')
    


class Annotaor(models.Model):
    team_name=models.ForeignKey(Team,on_delete=models.CASCADE)
    annotator_name=models.CharField(max_length=250)
    # LEAD_NAME=[
    #     ('Vinay/Pooja','vinay/pooja'),
    #     ('Rajan','rajan'),
    #     ('Guru','guru'),
    #     ('Gokul','gokul')
    # ]

    



class Quality_check(models.Model):
    id = models.AutoField(primary_key=True)
    Date=models.DateField(auto_now=False, auto_now_add=False)
    project_name=models.ForeignKey(Project,on_delete=models.CASCADE)
    task_type=models.ForeignKey(Project_types,on_delete=models.CASCADE)
    qualitycheck_by=models.ForeignKey(User,on_delete=models.CASCADE)
    annotator_name=models.ForeignKey(Annotaor,on_delete=models.CASCADE)
    clip_name=models.CharField(max_length=250)
    total_annotation=models.IntegerField()
    objects_checked=models.IntegerField()
    attibutes_error=models.IntegerField()
    geometry_precision_error=models.IntegerField()
    tracking_error=models.IntegerField()
    class_label_error=models.IntegerField()
    missing_error=models.IntegerField()
    unwanted_bbox_error=models.IntegerField()
    comments=models.CharField(max_length=250)


class Qualitycheck_Output(models.Model):
    id = models.AutoField(primary_key=True)
    attibute_percentage=models.CharField(max_length=50)
    geometry_percentage=models.CharField(max_length=50)
    tracking_percentage=models.CharField(max_length=50)
    tracking_percentage=models.CharField(max_length=50)
    class_percentage=models.CharField(max_length=50)
    missing_percentage=models.CharField(max_length=50)
    bbox_percentage=models.CharField(max_length=50)
    annotatorquality_percentage=models.CharField(max_length=50)
    qc_id=models.ForeignKey(Quality_check,on_delete=models.CASCADE)
