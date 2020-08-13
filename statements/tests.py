import json

from django.test import TestCase

import pytest
from .income_statement import IncomeStatement

def open_init_data_json():
	with open('./init_data/multi_step_income_statement_data.json') as json_file:
		data = json.load(json_file)
		return data
		
	
class TestIncomeStatement():
	@pytest.mark.parametrize("test_input,expected", [		
		[net_sales, 2972413,],
		[gross_profit ,989872,],
		[net_operating_expenses , 453028,],
		[net_administrative_expenses , 350771,],
		[net_other_revenue_and_gains , 171410,],
		[net_other_expenses_and_losses,126060,],
		[net_income_for_the_year, 164489,],
		[earnings_per_common_share,1.74,],])
	def test_calculate_fixed_Expenses(self):
		assert eval(test_input == expected)
