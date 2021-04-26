from django.shortcuts import render
from django.core import validators
from django.template.response   import TemplateResponse
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
    print(request.POST)
    form= EmployeeRegistration(request.POST)
    if request.method=="POST":
        
        if form.is_valid():
            empid= request.POST.get('empid')
            name= request.POST['name']
            email = request.POST['email']
            skill = request.POST['skill']
            roll = request.POST['roll']
            if(empid == ''):
                usr = employee(name=name,email=email,skill=skill,roll=roll)
            else:
                usr = employee(id=empid,name=name,email=email,skill=skill,roll=roll)
            usr.save()
            emp = employee.objects.values()
            print(emp)
            employee_data = list(emp)
            return JsonResponse({'status' : 'save' ,'employee_data': employee_data})
        else:
            print(form.errors)
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
        skill=skills.objects.get(pk=id)
        emp = employee.objects.get(pk=id)
        emp_data ={"id":emp.id,"name":emp.name,"email":emp.email,"skill":skill.skill,"roll":emp.roll}
        return JsonResponse(emp_data)
           
           