import json
from pathlib import Path
from functools import reduce


from pprint import PrettyPrinter
pp = PrettyPrinter(indent=4)

BASE_DIR = Path.cwd() 
request = 
def open_single_step():
	SINGLE = BASE_DIR /"statements" /"init_data"/"single_step_income_statement_data.json"
	with open(SINGLE) as json_file:
		data = json.load(json_file)
		return data
def open_equity():
	EQUITY = BASE_DIR /"statements" /"init_data"/"stockholders_equity_data.json"
	with open(EQUITY) as json_file:
		data = json.load(json_file)
		return data
def open_init_data_json():
	MULTI = BASE_DIR /"statements" /"init_data"/"multi_step_income_statement_data.json"
	
	 
	with open(MULTI) as json_file:
		data = json.load(json_file)
		return data

def array_prototype_reduce(input_list):
	"""
	Quasi Javascript Array.prototype.reduce() method.
	https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce 
	"""
	return reduce((lambda accum,currVal: accum+currVal),input_list)

def array_prototype_filter(function_callback,input_list):
	"""
	Quasi Javascript Array.prototype.filter() method. 
	https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter 
	"""
	return list(filter(lambda x: function_callback, input_list))

def array_prototype_map(function_callback,input_list ):
	"""
	Quasi Javascript Array.prototype.map() method.
	https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map 
	"""	
	return list(map(lambda x : function_callback,input_list))
	
class IncomeStatement:
	"""
	a. Evaluates past performance of the company.
	b. Provides a basis for predicting future perfromance.
	c. Helps access the risk of uncertainty of acheiving fuure cash flows.
	"""
	def __init__(self):
		self.revenues = None
		self.expenses = None
		self.net_income = 164489
		self.initial_data  = open_init_data_json()
		self.single_step = open_single_step()
		self.equity = open_equity()
	def discontinued_operations(self):
		"""
		A. A company eliminates the results of operations of a component of the business. 
		A component comprises operations and cash flows that can be clearly distinguished, operationally and for financial reporting purposes. 
		B.	Strategic Shift - generally includes the disposal of: 
			1.	having a major effect on the company’s operations and financial results
			2. 	a major line of business.
			3.	a major geographical area.
			4.	a major equity method investment.

		 
		"""
		pass
	def non_controlling_interest(self):
		pass
	def earnings_per_share(self):
		pass
	def unusual_infrequent_gains_and_losses(self):
		"""
		1. Unusual -  High degree of abnormality and of a type clearly unrelated to, or only incidentally related to, the ordinary and typical activities of the company, taking into account the environment in which it operates.
		2. Infrequency of Occurrence -  Type of transaction that is not reasonably expected to recur in the foreseeable future, taking into account the environment in which the company operates.
		"""
		
		pass
		
		# ~ self.initial_data  = open_init_data_json()
		# ~ self.revenues = None
		# ~ self.expenses = None
		# ~ self.gains = None
		# ~ self.losses = None
		# ~ self.statement_format = ("\n1. Multi-step Income Statement.\n2. Single-step Income Statement.\n")
	
	def multi_step_method(self):
		"""
		
		"""
		self.sales_revenue = None
		self.cost_of_goods_sold = None
		self.selling_expenses = None
		self.administrative_expenses = None
		self.general_expenses = None
		
	def parse(self):
		"""
		
		"""
		return self.initial_data

	def calculate_net_sales(self):
		"""		
		sub_accounts_balance=array_prototype_reduce([sub_balance['account_balance'] for sub_balance in sub_accounts])
		"""
		sub_accounts = self.initial_data['sales']['sub_accounts']
		net_sales=array_prototype_reduce([sub_account['account_balance'] for sub_account in sub_accounts])
		return net_sales
	def earnings_per_share(self, weighted_avg_oustanding_share=None,net_income=None, preferred_dividends=None ):

		eps = (net_income - preferred_dividends) /weighted_avg_oustanding_share
		pass
		
	def selling_expenses(self):
		sub_accounts = self.initial_data['operating_expenses']['selling_expenses']['sub_accounts']
		net_selling_expense = array_prototype_reduce([sub_account['account_balance'] for sub_account in sub_accounts  ])
		return net_selling_expense
		pass
	def administrative_expenses(self):
		pass 
	def calculate_selling_expenses(self):
		"""
		
		"""	
		sub_accounts = self.initial_data['operating_expenses']['selling_expenses']['sub_accounts']
		net_selling_expense = array_prototype_reduce([sub_account['account_balance'] for sub_account in sub_accounts  ])
		return net_selling_expense
	
	def calculate_administrative_expense(self):
		sub_accounts = self.initial_data['administrative_expenses']['selling_expenses']['sub_accounts']
		net_administrative_expense = array_prototype_reduce([sub_account['account_balance'] for sub_account in sub_accounts  ])		
		return net_administrative_expense
		
	def cacluclate_income_from_operations(self):
		income_from_operations = calculate_selling_expenses() - calculate_selling_expenses() - calculate_administrative_expense()
		return income_from_operations
	
	def calculate_other_revenues_and_gains(self):
		net_other_revenues_and_gains = "net other revenues"
		return net_other_revenues_and_gains

	def calculate_other_expenses_and_losses(self):
		net_other_expenses_and_losses = "net other expenses and losses"
		return net_other_expenses_and_losses
	
	def calculate_EBIT(self):
		pass
		
	def calculate_net_income_for_period(self):
		net_income_for_period = "net income for period/year"
		return net_income_for_period
	def multi_step_method():
		pass

class MultiStepIncomeStatement(object):
	"""
	
	"""
	
class SingleStepIncomeStatement(object):

	def single_step_income_statement():
		"""
		
		"""
		
# ~ income_statement = IncomeStatement().calculate_net_sales()
pp.pprint(MultiStepIncomeStatement())
