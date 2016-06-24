from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse
from reservas.models import *
# Create your views here.


def home(request):
	try:
		if request.user.temp_pass:
			return redirect(reverse("customers:password_change"))
		else:
			if Reserva.objects.filter(dueno=request.user).exists() or Reserva.objects.filter(inquilino=request.user).exists():
				for red in Reserva.objects.filter(dueno=request.user):
					if not red.califica_dueno:
						return redirect(reverse("reservas:my_list_rental",kwargs={"user_id":request.user.id})) 
				
				for rei in Reserva.objects.filter(inquilino=request.user):
					if not rei.califica_inquilino:
						return redirect(reverse("reservas:my_list_booking",kwargs={"user_id":request.user.id})) 
				return render(request,"home.html")
			else:
				return render(request,"home.html")
		#return redirect("hospedajes:list_recent")
	except Exception:
	#return redirect("customers:login")
		return render(request,"home.html")


def close_popup(request):
	return render(request, "close_popup.html")
