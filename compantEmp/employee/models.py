from django.db import models
#from multiselectfield import MultiSelectField
# Create your models here.
class employee(models.Model):
    Roll=(
        ('D','Developer'),
        ('T','Tester')
        )

   
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=90)
    skill=models.CharField(max_length=50)
    roll=models.CharField(max_length=1,choices=Roll)
    class Meta:
         db_table = "employee"  

 

class skills(models.Model):
   
    skill=models.ManyToManyField(employee)
    skills=models.CharField(max_length=50)
    class Meta:
         db_table = "skill"
   

class team(models.Model):
    team_name=models.CharField(max_length=50)
    team_leader_id=models.ForeignKey(employee,  on_delete=models.CASCADE)
    class Meta:
         db_table = "team"

