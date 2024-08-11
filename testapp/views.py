from django.shortcuts import render
from testapp.forms import EmployeeForm
# Create your views here.
def employee_view(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            print("record inserted.....!")
    form=EmployeeForm()
    return render(request,'testapp/StudentForm.html',{'form':form})