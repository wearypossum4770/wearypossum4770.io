import json

def open_init_data_json():
	with open('init_data.json') as json_file:
		data = json.load(json_file)
		return data



class TransAction(object):
	pass


class BalanceSheet:
	def __init__(self):
		self.current_assets = open_init_data_json()
		self.transaction_price = None
		self.valuation_method = input("\n1. Gross Method.\n2. Net Method\n")

	def calculate_net_accouts(self):
		return self.current_assets


	def recognition(self):
		"""
		1. Revenue Recognition Principle - revenues are recognized when the organization satisfies its performance obligation by transferring  goods or services to the customer.
		2. Performance Measures:
			a. Organization has the right to payment from client.
			b. Organization has passed legal title to the customer.
			c. Organization has transferred physical pocession of the goods.
			d. Organization no longer has significant risks and rewards of ownership of the goods.
			e. Client has accepted the asset.
		"""
		sales_returns_and_allowances = None
		trade_discount = None
		cash_discounts = sales_discounts = "discount"
		return sales_discounts

	def valuation(self, sales_discount = None, ):
		switch = {
			"1": (lambda x: x+3)(1),
			"2": (lambda x: x+3)(2),
			}
		value = switch.get(self.valuation_method,None)
		return value


	def disposition(self):
		pass

balance_sheet = BalanceSheet().recognition()
print(balance_sheet)
