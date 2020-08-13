from django.shortcuts import render
from accounts.models.amortization import Amortization
from accounts.views import AmortizationForm
# Create your views here.

def last_fiscal_year(request):
	pass

def amortization_schedule_view(request):
	"""
	TODO:
		1. Paginate Schedule.
		2. Create REACT Components.
	"""
	amount=schedule=None
	form = AmortizationForm()
	principal, interest_rate, number_of_periods,payment_frequency = form
	if request.mothod =="POST" and form.is_valid():
		amount = amortization_schedule.calculate_amortization_amount(principal, interest_rate / 100 / frequency, number_of_periods * frequency)
		schedule = list(amortization_schedule.amortization_schedule(principal, interest_rate / 100 / frequency, number_of_periods * frequency))
		context = dict([['amortization_amount',amount], ['amortization_schedule',schedule]])
		return render(request, context)
