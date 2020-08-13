import pytest
from accounts.models.annuity import Annuity


@pytest.mark.parametrize("principal, int_rate, num_periods, expected", [
(10000, .08, 3,2400.),
]
)
def test_simple_interest(principal:int, int_rate:float, num_periods:int, expected:float):
	new_annuity = Annuity(principal=principal,int_rate=int_rate,num_periods=num_periods	).simple_interest()
	assert new_annuity == expected
@pytest.mark.parametrize("principal, int_rate, num_periods, expected", [
(10000, .09, 1,10900.),
(10900, .09, 2,11881.),
(11881, .09, 3,12950.29),


]
)
def test_compound_interest(principal:int, int_rate:float, num_periods:int, expected:float)->float:
	new_annuity = Annuity(principal=principal,int_rate=int_rate,num_periods=num_periods	).compound_interest()
