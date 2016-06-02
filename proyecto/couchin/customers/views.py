import datetime
from django.shortcuts import redirect, get_object_or_404, render
from .models import Tarjeta, Customer
from .forms  import TarjetaForm, CustomerForm, CustomerDateForm, TarjetaDateForm, CustomerDateEditForm
from django.core.urlresolvers import reverse


# Create your views here
def select_account(request):
	return render(request, "user/select_account.html")

# Create your views here
def info_account(request,user_id):
	customer = get_object_or_404(Customer,id=user_id)
	return render(request, "user/info_account.html",{'customer':customer})

def update_premium(request, user_id):
	form = form = TarjetaDateForm(request.POST or None)
	print form.errors
	if form.is_valid():
		tarjeta = form.save(commit=False)
		tarjeta.fecha_venc_tarjeta = datetime.datetime(int(form.cleaned_data["ano"]), 
													   int(form.cleaned_data["mes"]),01)
		tarjeta.premiun_pago = "80"
		tarjeta.save()
		customer = Customer.objects.get(id=user_id)
		customer.tarjeta = tarjeta
		customer.fecha_premium = datetime.datetime.now()
		customer.premium = True
		customer.cliente = False
		customer.save()
		return render(request, "user/update_premium.html")
	return render(request, "user/update_premium.html", {"form":form})

def create_user_client(request):
	form = CustomerDateForm(request.POST or None)
	if form.is_valid():
		customer = form.save(commit=False)
		customer.cliente = True
		customer.set_password(form.cleaned_data["password"])
		customer.fecha_n = datetime.datetime(int(form.cleaned_data["ano"]), 
											 int(form.cleaned_data["mes"]),
											 int(form.cleaned_data["dia"]))
		customer.save()

		return redirect(reverse('customers:login'))
	return render(request, "user/create_user.html", {"form":form})


def update_user(request, user_id):
	customer = get_object_or_404(Customer, id=user_id)
	if request.method == 'POST':
		form = CustomerDateEditForm(data=request.POST, instance=customer)
		if form.is_valid():
			custo = form.save(commit=False)
			custo.fecha_n = datetime.datetime(int(form.cleaned_data["ano"]), 
											  int(form.cleaned_data["mes"]),
											  int(form.cleaned_data["dia"]))
			customer.save()
			return redirect(reverse('customers:info_account', kwargs={'user_id':user_id}))
	else:		
		form = CustomerDateEditForm(instance=customer)
		form.initial['ano'] = customer.fecha_n.year
		form.initial['mes'] = customer.fecha_n.month
		form.initial['dia'] = customer.fecha_n.day
		print form.initial
	return render(request, "user/update_user.html", {"form":form})




def admin_conf(request):
	return render(request, "admin/menu_admin.html")



