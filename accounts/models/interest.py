from re import findall
class Interest(object):
	__slots__ = ['principal','future_value','present_value' 'int_rate', 'num_periods', 'multiplier']

	def __init__(self,principal= None, interest_rate=None, time_periods=None):
		self._principal = principal
		self.int_rate = int_rate if type(int_rate) is float else int_rate/100
		self.num_periods = num_periods
		self.future_value = None
		self.present_value = None

def interest_rate_per_compounding_period(compound_frequency:str=None, interest_rate:int=None) ->float:
	switcher = {
		"a":(lambda x: (x/100)/1)(interest_rate),
		"s":(lambda x: (x/100)/2)(interest_rate),
		"q":(lambda x: (x/100)/4)(interest_rate),
		"m":(lambda x: (x/100)/12)(interest_rate),
		}
	value = switcher.get(compound_frequency)
	return value
	
def effective_rate_of_interest(interest_rate:int=None,time_periods:int = None )->float:
	effective_rate = pow((1+(interest_rate/100)),time_periods)-1
	return effective_rate
	

	
def number_compounding_periods():
	pass
	
def interest_compounded_continuously():
	pass
		
def future_value_single_sum(present_value:int=None,interest_rate:float=None, compound_frequency:int=None)->int:
	"""
	
	"""
	give_exact_value = False
	temp_future = present_value*pow((1+interest_rate),compound_frequency)
	# ~ return future_value if give_exact_value else round(give_exact_value)
	regexed_value = findall('([0-9]{0,})[.]([0-9]{1})([0-9]{0,})',str(temp_future))[0]
	future_value = 0
	if int(regexed_value[1]) > 4:
		future_value = int(regexed_value[0])+1
		return int(future_value)
	future_value = regexed_value[0]
	return int(future_value)
def present_value_single_sum(future_value:int=None,interest_rate:float=None, compound_frequency:int=None)->int:
	"""
	
	"""
	present_value_factor = 1/(pow((1+interest_rate),compound_frequency))
	temp_present = present_value_factor*future_value
	regexed_value = findall('([0-9]{0,})[.]([0-9]{1})([0-9]{0,})',str(temp_present))[0]
	present_value = 0
	if int(regexed_value[1]) > 4:
		present_value = int(regexed_value[0])+1
		return int(present_value)
	present_value = regexed_value[0]
	return int(present_value)

def compute_number_of_periods(present_value:int=None, future_value:int=None, interest_rate:int=None):
	"""
		Future Value Factor:

			formula_caluclation = 1.4640982200748782
			book_caclulation= 1.46410

		Present Value Factor:
		
			formula_calculation = 0.6830142857142857
			book_calculation = 0.68301
	"""
	by_future_value = True
	
	number_of_periods = future_value/present_value if by_future_value else present_value /future_value	
	return number_of_periods
	
print(compute_number_of_periods(present_value=47811, future_value=70000, interest_rate =.1))

def compute_interest_rate(present_value:int=None, future_value:int=None, compound_number:int=None):
	"""
	 book_calculation: 0.74726
	 formula_calculation: 0.7472557034291564
	"""
	by_future_value = True
	compound_number = future_value/present_value if by_future_value else present_value /future_value	
	return compound_number

print(compute_interest_rate(present_value=800000,compound_number=5,future_value= 1070584))
