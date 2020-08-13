# consider 

class Annuity(object):
	"""
	Calculates the relationship between time and money. One USD 
	received today is worth more than the same amount promised at some 
	time in the future.
	Present Value used to Measure:
		Accounts/Loans Receivable, Notes, Leases, Pensions, Post-Retirement 
		Benefits, long-term assets, stock-based compenstaion, business 
		combinations, disclosures, environmental liabilities.
	"""
	__slots__ = [
		'compound_frequency','num_compounding_periods','switcher',
		'future_value_factor','principal', 'int_rate', 'num_periods', 
		'multiplier', 'cash_flow',
		]
	
	def __init__(self, 
		principal:int=None, int_rate:float=None, num_periods:int=None, 
		compound_frequency:str=None, cash_flow:int=None)->None:
		self.cash_flow=cash_flow
		self.principal = principal
		self.int_rate = int_rate
		self.num_periods = num_periods
		self.multiplier = (1 + self.int_rate)
		self.switcher = {
			"a":(lambda x: (x/100)/1)(self.int_rate),
			"s":(lambda x: (x/100)/2)(self.int_rate),
			"q":(lambda x: (x/100)/4)(self.int_rate),
			"m":(lambda x: (x/100)/12)(self.int_rate),
			}
		self.num_compounding_periods = self.switcher.get(compound_frequency)


	def simple_interest(self)->int:
		try:
			interest = self.principal * self.int_rate * self.num_periods	
			if self.principal or self.int_rate or self.num_periods is None:
				raise TypeError(f"Required Values are:\nPrincipal:principal={type(self.principal)}\nInterest Rate:int_rate={type(self.int_rate)}\nNumber of Periods:num_periods={type(self.num_periods)}")
			return interest
		except TypeError as simpleError:
			print(simpleError)
	
	def compound_interest(self)->int:
		self.multiplier = (1 + self.int_rate)
		interest = self.principal * pow(self.multiplier, self.num_periods)
		return interest
		
	def calculate_amortization_amount(self.principal, self.int_rate, self.num_periods):
		x = (1 + self.int_rate) ** period
		return principal * (self.int_rate * x) / (x - 1)
	def present_value_perpetuity(self)->float:
		"""
		Is the same as annuity, but no ending period, it is infinite.
		"""
		try:
			perpetuity_value=self.cash_flow / self.int_rate
			if self.cash_flow or self.int_rate is None:
				raise TypeError (f"Required Values are Cash Flow (Periodic Payment):cash_flow={type(self.cash_flow)}\nInterest Rate:int_rate={type(self.int_rate)})")
			return perpetuity_value
		except TypeError as perpetuityError:
			print(perpetuityError)
	def present_value_annuity_due(self):
		# PVAD = P + P [ (1 - (1 + r) ^(- (n - 1)) ) ÷ r ]
	def future_value_end_of_period(self)->float:
		#2875.3695050000024
		try:
			self.future_value_factor = pow(self.multiplier,self.num_periods)
			annuity_future_value = self.cash_flow * ((self.future_value_factor -1)/ self.int_rate)
			if self.cash_flow  or self.num_periods or self.int_rate is None:
				raise TypeError (f"Required Values are Interest Rate:int_rate={type(self.int_rate)}")
			return annuity_future_value
		except TypeError as futureValueError:
			print(futureValueError)
	
	def future_value_ordinary(self):
		"""
		
		"""
new_annuity = Annuity(cash_flow=500,int_rate=.06).present_value_perpetuity()
#8333.333333333334
# ~ new_annuity = Annuity(cash_flow=100,int_rate=.07, num_periods=5).present_value_perpetuity()
print(new_annuity)
