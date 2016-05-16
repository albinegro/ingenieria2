from django.shortcuts import redirect, render

# Create your views here.


def home(request):
    #if request.user.is_authenticated():
        #return redirect("orders:list")
    #return redirect("customers:login")
    return render(request,"base.html")
    {% url 'customers:login' %}

def close_popup(request):
    return render(request, "close_popup.html")
