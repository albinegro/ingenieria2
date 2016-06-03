from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse
# Create your views here.


def home(request):
	try:
		if request.user.temp_pass:
			return redirect(reverse("customers:password_change"))
		else:
			return render(request,"home.html")
		#return redirect("hospedajes:list_recent")
	except Exception:
	#return redirect("customers:login")
		return render(request,"home.html")


def close_popup(request):
	return render(request, "close_popup.html")
