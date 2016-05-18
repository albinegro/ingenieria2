from django.shortcuts import render

# Create your views here.


def create_user(request):
	if request.method =="POST":
	    form = CustomerForm(data=Customer,request.POST)
	    if form.is_valid()
	form = CustomerForm()
	return render(request, "user/create_user.html", {"form":form})

