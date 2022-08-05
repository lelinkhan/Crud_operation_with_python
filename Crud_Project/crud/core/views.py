from django.shortcuts import render, redirect
from django.views import View
from .models import Student
from .forms import AddStudentForm
# Create your views here.

class Home(View):
    def get(self,request):
        student_data = Student.objects.all()
        return render(request,'core/home.html',{'student_data':student_data})


class Add_student(View):
    def get(self,request):
        fm = AddStudentForm()
        return render(request,'core/add_student.html',{'form':fm})

    def post(self,request):
        fm = AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request,'core/add_student.html',{'form':fm})

class Delete_student(View):
    def post(self,request):
        data = request.POST
        id = data.get('id')
        student_data = Student.objects.get(id = id)
        student_data.delete()
        return redirect('/')

class Edit_student(View):
    def get(self,request,id):
        student_data = Student.objects.get(id = id)
        fm = AddStudentForm(instance=student_data)
        return render(request,'core/edit_student.html',{'form':fm})

    def post(self,request,id):
        student_data = Student.objects.get(id = id)
        fm = AddStudentForm(request.POST,instance=student_data)
        if fm.is_valid():
            fm.save()
            return redirect('/')