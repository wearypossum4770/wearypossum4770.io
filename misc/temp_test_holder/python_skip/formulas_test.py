import pytest
from core.formulas import contribution_margin, calculate_contribution_margin_ratio

 
@pytest.mark.parametrize("test_input,expected", [((1250000,1020000),230000), ((3600000,3015000),585000),((2380000,2142000),238000)])
def test_contribution_margin(test_input,expected):
	sales_revenue, variable_cost = test_input
	test_case = contribution_margin(sales_revenue, variable_cost)
	assert test_case == expected
