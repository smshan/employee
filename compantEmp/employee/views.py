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
    skill=skills.objects.all()
    form= EmployeeRegistration(request.POST)
    if request.method=="POST":
        if form.is_valid():
            empid= request.POST.get('empid')
            name= request.POST['name']
            email = request.POST['email']
            skill = request.GET.get('skill')
            roll = request.POST['roll']
            if(empid == ''):
                usr = employee.objects.all()
            else:
                usr = employee.objects.all()
            usr.save()
            emp = employee.objects.values()
            print(emp)
            employee_data = list(emp)
            return JsonResponse({'status' : 'save' ,'employee_data': employee_data})
        else:
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
        return JsonResponse(emp_data)
           
