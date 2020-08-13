from django.core.validators import MaxValueValidator
from datetime import datetime
from django.db.models import (
Model, ForeignKey, CASCADE,DecimalField, PositiveSmallIntegerField,
DateField,BooleanField,CheckConstraint,Q
)
from django.utils.translation import gettext_lazy as _

class AssetLifecycle(Model):
	class Status():
		ACQUIRED = "ACQ", _('Asset Purchase / Not In Use')
		IN_USE = "USE", _('Current Asset / In Use')
		DISPOSED = "DEL", _('Asset Disposed of')
		__empty__ = _('(Unknown Status)')
	lifecycle_name = CharField(max_length=50)
	lifecycle_description = CharField(max_length=50)
	lifecycle_status = CharField(max_length=3, choices=Status.choices, default = Status.__empty__)
	
class Asset(Model):
	lifecycle = ForeignKey(AssetLifecycle, on_delete=CASCADE)
	alternate_name = CharField(max_length=20)
	disambiguating_description = CharField(max_length=20)
	market_price = DecimalField(max_digits=9,decimal_places=2)
	currency = CharField(max_length=3, default="USD")
	received_date = DateField()
	useful_life = PositiveSmallIntegerField(validators = [MaxValueValidator(20, message="Unusual product life - greater than 20 years.")])
	residual_value = DecimalField(max_digits=9,decimal_places=2, default=0.00)
	net_value = DecimalField(max_digits=9,decimal_places=2)
	serial_number = CharField(max_length=50, null=True, blank=True)
	is_current_asset = BooleanField(default=True)
	asset_type = CharField(max_length=5)
	disposal_date = DateField()
	class Meta:
		constraints = [
		CheckConstraint(
		check=Q(disposal_date__gte=received_date), name='disposal_date_gte_received_date')
		)
		]
	def disposal_of_asset(self):
		return self.disposal_date = datetime.now()
		
	def calculate_amortization_amount(principal, interest_rate, period):
		x = (1 + interest_rate) ** period
		return principal * (interest_rate * x) / (x - 1)
		
	def amortization_schedule(principal, interest_rate, period):
		amortization_amount = calculate_amortization_amount(principal, interest_rate, period)
		number = 1
		balance = principal
		while number <= period:
			interest = balance * interest_rate
			principal = amortization_amount - interest
			balance = balance - principal
			yield number, amortization_amount, interest, principal, balance if balance > 0 else 0
			number += 1
