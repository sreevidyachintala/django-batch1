from django.shortcuts import render,redirect

from django.http import HttpResponse
from app1.forms import RegisterForm

from .models import Register

from django.contrib import messages

# Create your views here.

def dynamic(request):
	return HttpResponse("Welcome Formsapp")


def register(request):
	if request.method == 'POST':
		f=RegisterForm(request.POST)
		if f.is_valid():
			f.save()
			#return HttpResponse("Done")
			messages.success(request,"successfully registered")

			return redirect('display')
	f=RegisterForm()
	return render(request,"app1/register.html",{'form':f})

def display(request):
	data = Register.objects.all()
	return render(request,'app1/display.html',{'data':data})


def update(request,id):
	w=Register.objects.get(id=id)
	if request.method == 'POST':
		form = RegisterForm(request.POST,instance=w)
		if form.is_valid():
			form.save()
			#return HttpResponse('Updated')
			messages.success(request,"Updated ssuccessfully")
			return redirect('display')
	form=RegisterForm(instance=w)
	return render(request,'app1/update.html',{'form':form,'w':w})


def delete(request,id):
	ob = Register.objects.get(id=id)
	if request.method == 'POST':
		ob.delete()
		#return HttpResponse('deleted')
		messages.success(request,"successfully Deleted")
		return redirect('display')
	return render(request,'app1/delete.html',{'ob':ob})