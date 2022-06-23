from django.shortcuts import render  
from django.http import HttpResponse  
from .forms import StudentForm  

def handle_uploaded_file(f):  
    with open('employeeApp/static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  
import json    
def index(request):  
    if request.method == 'POST': 
        print(request.POST) 
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            dict = {'msg':"success"}
            return HttpResponse(json.dumps(dict), content_type='application/json')
        dict = {'msg':"Failed"}
        return HttpResponse(json.dumps(dict), content_type='application/json')
        # return HttpResponse("File uploaded successfuly") 
            
    else:  
        print("in else");
        student = StudentForm()  
        return render(request,"employeeApp/index.html",{'form':student})