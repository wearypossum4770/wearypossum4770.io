def issue_loan():
	loan_info = {
	"loanPrinciple":1000,
	"journal_entry_method":"net",
	"loanPaymentAmount":0,
	"when_recorded": 1596814920911,
	"when_received":1597678920000,
	"loanTerm": {"discount":2,"annualPercentageRate":0,"paidWithin":10,"netDue":30}
	}
	
	regular_rate = loan_info['loanPrinciple']
	discounted_rate = (1-loan_info['loanTerm']['discount']/100)*loan_info['loanPrinciple']
	
	if loan_info['journal_entry_method'] is 'net':
		
		journal_entry = {
		"debit_account":"accounts_recievables", "debit_amount":discounted_rate,
		"credit_account":"sales_revenue","credit_amount":discounted_rate
		}
	
	else:
		
		journal_entry = {
		"debit_account":"accounts_recievables", "debit_amount":regular_rate,
		"credit_account":"accounts_recievables","credit_amount":regular_rate
		}
	
def loan_payment():
	loan_info = {
	"loanPrinciple":1000,
	"journal_entry_method":"net",
	"loanPaymentAmount":0,
	"when_recorded": 1596814920911,
	"when_received":1597678920000,
	"loanTerm": {"discount":2,"annualPercentageRate":0,"paidWithin":10,"netDue":30}
	}
	discount_end_of_life loan_info['loanTerm']['paidWithin']
	paid_in_discount_period = (timedelta(milliseconds = loan_info['when_received'])- timedelta(milliseconds = loan_info['when_recorded']) ).days <=discount_end_of_life
	regular_rate = loan_info['loanPrinciple']
	discounted_rate = (1-loan_info['loanTerm']['discount']/100)*loan_info['loanPrinciple']
	if paid_in_discount_period and loan_info['journal_entry_method']=='net':
	
		journal_entry = {
		"debit_account":"cash", "debit_amount":regular_rate,
		"credit_account":"accounts_recievables","credit_amount":regular_rate
		}
	
	elif not paid_in_discount_period and loan_info['journal_entry_method']=='net':
		journal_entry = {
		"debit_account1":"cash", "debit_amount":loan_info['loanPrinciple'],
		"debit_account1":"accounts_recievables", "debit_amount":discounted_rate,
		"credit_account":"interest_revenue","credit_amount":regular_rate - discounted_rate
		}
	
	elif paid_in_discount_period and loan_info['journal_entry_method']=='gross':
		journal_entry = {
		"debit_account1":"cash", "debit_amount":regular_rate - discounted_rate,
		"credit_account1":"cash_discounts", "debit_amount":discounted_rate,
		"credit_account2":"accounts_receivables","credit_amount": regular_rate
		}	
	else :
		journal_entry = {
		"debit_account":"cash", "debit_amount":regular_rate,
		"credit_account":"accounts_recievables","credit_amount":regular_rate
		}
