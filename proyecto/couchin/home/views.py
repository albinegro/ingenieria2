from django.shortcuts import redirect, render

# Create your views here.


def home(request):
    #if request.user.is_authenticated():
        #return redirect("hospedajes:list_recent")
    #return redirect("customers:login")
    return render(request,"base.html")


def close_popup(request):
    return render(request, "close_popup.html")
