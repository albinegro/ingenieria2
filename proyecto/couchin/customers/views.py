import string
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import csrf_exempt
from core.libs import check_temporal
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from django.shortcuts import redirect, get_object_or_404, render, resolve_url
from .models import Tarjeta, Customer
from .forms  import TarjetaForm, CustomerForm, CustomerDateForm, TarjetaDateForm, CustomerDateEditForm, ResetEmailForm
from django.core.urlresolvers import reverse
from random import sample, choice
from django.template.response import TemplateResponse
from django.contrib.auth import  update_session_auth_hash

from django.contrib.auth.forms import PasswordChangeForm
chars = string.letters + string.digits

@login_required
def password_change(request,
					template_name='registration/password_change_form.html',
					post_change_redirect=None,
					password_change_form=PasswordChangeForm,
					current_app=None, extra_context=None):
	if post_change_redirect is None:
		post_change_redirect = reverse('password_change_done')
	else:
		post_change_redirect = resolve_url(post_change_redirect)
	if request.method == "POST":
		form = password_change_form(user=request.user, data=request.POST)
		if form.is_valid():
			form.save()
			customer = Customer.objects.get(id=request.user.id)
			if customer.temp_pass:
				customer.temp_pass = False
				customer.save()
			# Updating the password logs out all other sessions for the user
			# except the current one if
			# django.contrib.auth.middleware.SessionAuthenticationMiddleware
			# is enabled.
			update_session_auth_hash(request, form.user)
			return HttpResponseRedirect(post_change_redirect)
	else:
		form = password_change_form(user=request.user)
	context = {
		'form': form,
		'title': _('Password change'),
	}
	if extra_context is not None:
		context.update(extra_context)

	if current_app is not None:
		request.current_app = current_app

	return TemplateResponse(request, template_name, context)



def reset_password(request):
	form = ResetEmailForm(request.POST or None)
	if form.is_valid():
		customer = Customer.objects.get(email=form.cleaned_data["email"])
		customer.temp_pass= True
		customer.set_password(form.cleaned_data["uuid"])
		customer.save()
		return redirect(reverse("customers:login"))
	cont = ''.join(choice(chars) for _ in range(8))
	form.initial['uuid'] = cont
	return render(request, "password/reset.html", {"form":form, "cont_temporal":cont})

@login_required
@user_passes_test(check_temporal)
# Create your views here
def select_account(request):
	return render(request, "user/select_account.html")


# Create your views here
@login_required
@user_passes_test(check_temporal)
def info_account(request,user_id):
	customer = get_object_or_404(Customer,id=user_id)
	return render(request, "user/info_account.html",{'customer':customer})

@login_required
@user_passes_test(check_temporal)
@csrf_exempt
def update_premium(request, user_id):
	form = form = TarjetaDateForm(request.POST or None)
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

@login_required
@user_passes_test(check_temporal)
@csrf_exempt
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



@login_required
@user_passes_test(check_temporal)
def admin_conf(request):
	return render(request, "admin/menu_admin.html")



