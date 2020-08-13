from django.core.validators import MinValueValidator,MaxValueValidator
from accounts.models import Account
from core.validation_messages import amortization_validation_msg as msg


class Amortization(Account):
	class Frequency:
		ANNUAL =1 ,_("")
		SEMIANUAL= 2,_("")
		QUARTERLY= 4,_("")
		BI_MONTHLY=6, _("")
		MONTHLY= 12,_("")
		BI_WEEKLY= 24,_("")
		WEEKLY= 52,_("")
		DAILY= 360,_("")
		CONTINUOUS= "inf",_("")
		__empty__ = _("(Unknown)")
	principal=DecimalField(
		max_digits = 9,
		decimal_places=2,
		validators = [
			(MinValueValidator(0,message=msg.get('princ_min')))
			]
		)
	interest_rate=DecimalField(
		max_digits = 5,
		decimal_places=2,
		validators = [
			(MinValueValidator(0,message=msg.get('int_rate_min'))),
			(MaxValueValidator(100.00,message=msg.get('int_rate_max')))
			]
		)
	number_of_periods = PositiveSmallIntegerField(	validators = [
			(MinValueValidator(0,message=msg.get('num_period_min')))
			])
	payment_frequency = CharField(max_length=2,choices=Freqency.choices, default=Frequency.MONTHLY)

	def calculate_amortization_amount(self):
		x = (1 + self.interest_rate) ** self.number_of_periods
		return self.principal * (self.interest_rate * x) / (x - 1)
	def amortization_schedule(self.principal, self.interest_rate, self.number_of_periods):
		amortization_amount = self.calculate_amortization_amount(self.principal, self.interest_rate, self.number_of_periods)
		number = 1
		balance = self.principal
		while number <= self.number_of_periods:
			interest = balance * self.interest_rate
			principal = amortization_amount - self.interest
			balance = balance - self.principal
			yield number, amortization_amount, self.interest, self.principal, balance if balance > 0 else 0
			number += 1
	def fetch_capatcha(self):
		pass
	
	def fetch_recapatcha(self):
		pass


    
