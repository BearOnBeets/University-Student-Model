from django.shortcuts import render
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from urllib import response
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Student,University
import json


def index(request):
    #To test whether the app is running
    return HttpResponse("The APP is running")  

#to remove csrf forbiddden error
@csrf_exempt          
def createuniversity(request):
    if(request.method=='POST'):
        university_name=request.POST['university_name']
        location=request.POST['location']
        db=University(university_name=university_name,location=location)
        db.save()
        return HttpResponse("University Created Successfully")
    else:
        #Error if called with GET method
        return HttpResponse("You need to POST this API")

def alluniversity(request):
    #getting queryset containing all the universities
    qs=University.objects.all().values()        
    #universities=serializers.serialize('json', qs)
    #converting it into JSON using JSON.dumps. The Serialize() method will not work here as i have used the .values() method to fetch only the values and hide the db details. 
    universities = json.dumps(list(qs))         
    return HttpResponse(universities)

@csrf_exempt
def create(request):
    if(request.method=='POST'):
        name=request.POST['name']
        course=request.POST['course']
        grade=request.POST['grade']
        try:
            #Checking if the entered university exists or not? If it exists we save it in a variable
            university=University.objects.get(university_name=request.POST['university'])
        except University.DoesNotExist:
            return HttpResponse("University Does Not Exist")
        
        db=Student(name=name,course=course,grade=grade,university=university)
        db.save()
        return HttpResponse("Student Created Successfully")
    else:
        return HttpResponse("You need to POST this API")

def all(request):
    qs=Student.objects.all().values()
    #again serializing with json.dump
    students = json.dumps(list(qs))
    #converting json string to list
    students=json.loads(students) 
    for i in students:
        university=University.objects.get(id=i['university_id'])
        #adding university details to student list
        i['university_name']=university.university_name
        i['university_location']=university.location
    return HttpResponse(students)     

@csrf_exempt
def update(request):
    if(request.method=='POST'):
        try:
            # checking if student with the entered id exists
            student=Student.objects.get(id=request.POST['id'])
        except Student.DoesNotExist:
            return HttpResponse("Student Does Not Exist!")

        name=request.POST['name']
        course=request.POST['course']
        grade=request.POST['grade']
        try:
            university=University.objects.get(university_name=request.POST['university'])
        except University.DoesNotExist:
            return HttpResponse("University Does Not Exist")
        
        #updating student obj here 
        student.name=name
        student.grade=grade
        student.course=course
        student.university=university
        student.save()
        return HttpResponse("Student Updated Successfully")
    else:
        return HttpResponse("You need to POST this API")

@csrf_exempt
def delete(request):
    if(request.method=='POST'):
        try:
            student=Student.objects.get(id=request.POST['id'])
        except Student.DoesNotExist:
            return HttpResponse("Student Does Not Exist!")
        student.delete()
        return HttpResponse("Student Deleted Successfully")
    else:
        return HttpResponse("You need to POST this API")