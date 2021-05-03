from django.shortcuts import render
from django.core import validators
from django.template.response   import TemplateResponse
import simplejson as json
from django.http import JsonResponse

#from django.views.decorators.csrf import csrf_exempt
from .forms import EmployeeRegistration
from .models import employee,skills
# Create your views here.
def addemployee(request):
    skill = skills.objects.all()
    emp = employee.objects.all()
    fm = EmployeeRegistration()
    return render(request,'index.html',{'form':fm,'em': emp,'sk':skill})
#@csrf_exempt
def save_data(request):
    
    form= EmployeeRegistration(request.POST)
    if request.method=="POST":
        name= request.POST['name']
        skillid=request.POST['skill']
        email = request.POST['email']
        roll = request.POST['roll']
        print(request.POST)
     #
        usr = employee(name=name,email=email,roll=roll)
        usr.save()

        for skill in skillid:
           usr.skill.add(skills.objects.get(id=skill))
        return json.dumps({'status' : 'save','usr':usr })
    else:     
        print(request.POST) 
        return JsonResponse({'status' : 0})
#delete data
def delete_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        #print(id)
        pi = employee.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})
           
#edit data
def Edit_data(request):
  
    if request.method == "POST":
        
        id = request.POST.get('sid')

        print(id)
        emp = employee.objects.get(pk=id)
       
        emp_data ={"id":emp.id,"name":emp.name,"email":emp.email,"skill":emp.skill,"roll":emp.roll}
       
        return Json.dumps(emp_data)
           
