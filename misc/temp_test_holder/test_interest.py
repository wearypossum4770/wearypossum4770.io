from re import findall
import pytest
from accounts.models.interest import (
Interest,future_value_single_sum, present_value_single_sum,
compute_number_of_periods,compute_interest_rate
)

class TestInterest:

	@pytest.mark.parametrize("present_value, interest_rate, compound_frequency, expected", [
	(50000, .06, 5,66911),
	(250000000,.05,8,369363861),
	]
	)
	def test_future_value_single_sum(self,present_value:int, interest_rate:float, compound_frequency:int, expected:int)->int:
		test_exact_value=future_value_single_sum(present_value=present_value,interest_rate=interest_rate,compound_frequency=compound_frequency)
		assert test_exact_value==expected
	
	@pytest.mark.parametrize("future_value, interest_rate, compound_frequency, expected", [
	(73466, .08, 5,50000.),
	]
	)
	def test_present_value_single_sum(self,future_value:int, interest_rate:float, compound_frequency:int, expected:int)->int:
		test_exact_value=present_value_single_sum(future_value=future_value,interest_rate=interest_rate,compound_frequency=compound_frequency)
		assert test_exact_value==expected
	
	@pytest.mark.parametrize("present_value, interest_rate, future_value, compound_frequency", [
	(47811, .1, 70000,1.4640982200748782),
	]
	)
	def test_compute_number_of_periods(self,present_value:int, future_value:int, interest_rate:int, compound_frequency:float)->float:

		test_exact_value=compute_number_of_periods(future_value=future_value,interest_rate=interest_rate,present_value=present_value)
		
		assert test_exact_value==compound_frequency
	@pytest.mark.parametrize("present_value, compound_number, future_value, interest_rate", [
	(800000,5, 1070584,1.33823),
	]
	)

	def test_compute_interest_rate(self,present_value:int, future_value:int, compound_number:int,interest_rate:float)->float:

		test_exact_value=compute_interest_rate(future_value=future_value,compound_number=compound_number,present_value=present_value)
		
		assert test_exact_value==interest_rate

#recover uncollectible account
# Accounts Recievable (Randall Co.)			1,000
#    Allowance for Doubtful Accounts				1,000
# Cash 										1,000
#	Accounts Receivable (Randall Co.)				1,000
