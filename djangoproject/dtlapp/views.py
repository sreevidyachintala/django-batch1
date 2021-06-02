from django.shortcuts import render,redirect

from .forms import UserReg,Uppro,imagepro

from django.contrib.auth.decorators import login_required



# Create your views here.

def home(request):
	return render(request,'dtlapp/home.html')

def about(request):
	return render(request,'dtlapp/about.html')

def contact(request):
	return render(request,'dtlapp/contact.html')

@login_required
def dashboard(request):
	return render(request,'dtlapp/dashboard.html')

def profile(request):
	return render(request,'dtlapp/profile.html')

def uppro(request):
	if request.method == 'POST':
		t=Uppro(request.POST,instance=request.user)
		y=imagepro(request.POST,request.FILES,instance=request.user.update)
		if t.is_valid() and y.is_valid():
			t.save()
			y.save()
			
			return redirect('profile')
	t=Uppro(instance=request.user)
	
	y=imagepro(instance=request.user.update)
	return render(request,'dtlapp/uppro.html',{'t':t,'y':y})

def register(request):
	if request.method == 'POST':
		form = UserReg(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	form = UserReg()
	return render(request,'dtlapp/register.html',{'form':form})