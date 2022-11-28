from django.shortcuts import render,HttpResponse ,redirect      
from emp_app.models import emp
# from .forms import EmployeeForm

# Create your views here.
def index(request):
    # emps = emp.objects.all()
    # context={'emps':emps} 
    return render(request,"home.html")


def all_emp(request):
    emps = emp.objects.all()
    context={'emps':emps} 
    # emps = emp.objects.all()
#     # context={'emps':emps}
    
   
    return render(request,"index.html",context)



def add_emp(request):
    # emps = emp.objects.all()
    # print(emps)
    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salary=int(request.POST['salary'])
        dept=request.POST['dept']
        new =emp(first_name=first_name,last_name=last_name,salary=salary,dept=dept)
       
        new.save()
       
        return HttpResponse("successfuly added")
    else:
        return render(request,"add_emp.html")

def edit_emp(request,emp_id):
     
    emps=emp.objects.get(id=emp_id)
    
    context={'emps':emps} 
    
    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salary=int(request.POST['salary'])
        dept=request.POST['dept']
        
        emps =emp(first_name=first_name,last_name=last_name,salary=salary,dept=dept)
       
        emps.save()
        return redirect("all_emp")
     

    else:
        print("else")
        return render(request,'edit_emp.html',context)



def delete_emp(request,emp_id):
    # emps = emp.objects.all()
    # context={'emps':emps} 
    if emp_id:
     emp_del= emp.objects.get(id=emp_id)
     emp_del.delete()
     return HttpResponse("successfuly deleted")
    else:
        return render(request,"index.html")



# def create_emp(request):
#     form = EmployeeForm()

#     if request.method == 'POST':
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('employees-list')

#     context = {
#         'form': form,
#     }
#     return render(request, 'employee/create.html', context)



