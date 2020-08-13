# ~ BaseURL/v3/company/1386066315/reports/
# ~ AccountList?
# ~ columns=account_name,
# ~ account_type&
# ~ account_type=Income

# ~ BaseURL/v3/company/1386066315/reports/
# ~ AgedReceivableDetail?
# ~ report_date=2015-06-30&
# ~ start_duedate=2015-01-01&
# ~ end_duedate=2015-06-30
# ~ &columns=due_date,
# ~ cust_name


# ~ BaseURL/v3/company/1386066315/reports/
# ~ AgedReceivables?customer=4&
# ~ date_macro=Last Fiscal Year

from django.forms import ModelForm

class AmortizationForm(ModelForm):
	class Meta:
		model = Account
		fields = [
			'principal','interest_rate',
			'number_of_periods','payment_frequency',
			]
	
