import json

from django.test import TestCase

import pytest
from statements.income_statement import IncomeStatement
		
	
class TestIncomeStatement():
	"""
	@pytest.mark.parametrize("test_input,expected", [		
		[net_sales, 2972413,],
		[gross_profit ,989872,],
		[net_operating_expenses , 453028,],
		[net_administrative_expenses , 350771,],
		[net_other_revenue_and_gains , 171410,],
		[net_other_expenses_and_losses,126060,],
		[net_income_for_the_year, 164489,],
		[earnings_per_common_share,1.74,],])
	"""

	def test_calculate_gross_profit(self):
		test_case = IncomeStatement().calculate_net_sales()
		expected = 2972413
		assert test_case == expected
	def test_earnings_per_share(self):
		test_case = IncomeStatement().earnings_per_share()

		weighted_avg_oustanding_share = 50000
		net_income = 30000
		preferred_dividends = 4000
	# ~ def test_calculate_selling_expenses(self):
		# ~ test_case = IncomeStatement().calculate_selling_expenses()
		# ~ expected = 453028
		# ~ assert test_case == expected
	
	# ~ def test_calculate_administrative_expense(self):
		# ~ test_case = IncomeStatement().calculate_administrative_expense()
		# ~ expected = 350771
		# ~ assert test_case == expected
	
	# ~ def test_cacluclate_income_from_operations(self):
		# ~ test_case = IncomeStatement().cacluclate_income_from_operations()
		# ~ expected = 186073
		# ~ assert test_case == expected
	
	# ~ def test_calculate_net_income_for_period (self):
		# ~ test_case = IncomeStatement().cacluclate_income_from_operations()
		# ~ expected = 125060
		# ~ assert True == True
	# ~ def test_calculate_EBIT(self):
		# ~ test_case = IncomeStatement().cacluclate_income_from_operations()
		# ~ expected = 231423
		# ~ assert True == True
	# ~ def test_calculate_other_expenses_and_losses(self):
		# ~ test_case = IncomeStatement().cacluclate_income_from_operations()
		# ~ expected = 186073
		# ~ assert True == True
