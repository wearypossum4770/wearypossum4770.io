class Valuation(object):
	"""
	principal: float= None
		enter dollar amount with decimal.
	interest_rate: float=None
		can bet integer or float
	time_periods:int = None
		Enter in time in years:
		One Month
			30/360
			1/12
	"""
	def __init__(self,principal= None, interest_rate=None, time_periods=None):
		self._principal = principal
		self._interest_rate = interest_rate if type(interest_rate) is float else interest_rate/100
		self._time_periods = time_periods
	
	# ~ def compound_interest(self,__principal: float=None, __interst_rate: float = None, __time: float = None )-> float:
		# ~ self._principal = __pricipal
		# ~ self._interest_rate = __interest_rate
		# ~ self._time = __time		
		
	def compound_interest(self):
		"""
		
		"""
		
	def simple_interest(self):
		"""
		
		Return the principle and interest as a dictionary.
	
		"""
		simple_interest =  self._principal * self._interest_rate * self._time_periods

	def future_value_of_one(self, value_of_period = None):
		"""

		"""
		value_of_period = 
		self.future_value = pow((1+self._interest_rate),self._time_periods)
		
		
		return self.future_value
	def present_value_of_one(self):
		"""

		"""

	def future_value_ordinary_annuity(self):
		"""

		"""

	def present_value_of_ordinary_annuity(self):
		"""

		"""

	def present_value_annuity_due(self):
		"""

		"""
	def calculate_amortization_amount(self,principal, interest_rate, period):
		"""
		
		"""
		
		formula = (1+interest_rate) **period
		return principal* (interest_rate * formula) / (formula -1)
	
	
	def generate_interest_rate_table(self):
		"""
		creates an interest rate table in csv or json
		"""
		header_row = ('Period','Period Amount(Beginning)', 'Period Amount(Ending)', )
		rows_array = []
		
		for period_index in range(self.time_periods):
			value_of_period =  pow((1+self._interest_rate),period_index)

			row_data = (period_index, ,value_of_period)
		
		
new_loan = Valuation(principal=1,interest_rate=5,time_periods=3).future_value_of_one()
print(new_loan)
