from django.db import models
from django.forms import ModelForm
from django.core import validators
#from multiselectfield import MultiSelectField
# Create your models here.

class skills(models.Model):
   
    skill=models.CharField(max_length=50)
    def __unicode__(self):
        return self.skill
 

    def __str__(self):
        return self.skill 


class employee(models.Model):
    Roll=(
        ('D','Developer'),
        ('T','Tester')
        )
   
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=90)
    skill=models.ManyToManyField(skills)
    roll=models.CharField(max_length=1,choices=Roll)
    def __str__(self):
        return self.name
        return self.email
        return self.skill
        return self.roll
    

 
class team(models.Model):
    team_name=models.CharField(max_length=50)
    team_leader_id=models.ForeignKey(employee,  on_delete=models.CASCADE)
    def __str__(self):
        return self.team_name
        return self.team_leader_id
 

