values = {
	"DOM_MAX":"No More than 31 days in any month. Please check value.",
	"DOM_MIN": "Months must start with 1, no negative indexing is allowed.Please check value.",
	"SALES_DIS_MIN":"Sales discount cannot be negative. This would charge extra fees to transaction.",
	"SALES_DIS_MAX":"Sales discount cannot be greater than 100. This would leave a blance owed to customer.",
	}

class Schedule:
	class DaysOfWeek:
		MON = 1, _('Monday')
		TUE=2, _('Tuesday')
		WED=3, _('Wednesday')
		THUR=4, _('Thursday')
		FRI=5, _('Friday')
		SAT=6, _('Saturday')
		SUN = 7, _('Sunday')
	class Frequency:
		DAILY = 1
		WEEKLY = 7
		BI_WEEKLY 14
		MONTHLY = 30
		BI_MONTHLY = 60
		QUARTERLY  = 90
		SEMI_ANNUAL= 180
		ANNUAL = 360
		__empty__ = _("One-Time Transaction")
	class Method:
		AUTO = ""
		MAN= ""
		MIND = ""
		NON = ""
	start_date = DateField()
	end_date = DateField()
	days_before= 
	day_of_month= Integer(validators = [
		MaxValueValidator(31, message=values.get('DOM_MAX')),
		MinValueValidator(1, message= values.get('DOM_MIN'))
		])
	day_of_week = CharField(max_length=1, choices=DaysOfWeek.choices)
	previous_transaction = DateTime()
	next_transaction = DateTime()
	interval = CharField(max_length=3, choices=Frequency.choices, default=Frequency.__empty__)
	day_of_month = Integer(validators = [
		MaxValueValidator(31, message=values.get('DOM_MAX')),
		MinValueValidator(1, message= values.get('DOM_MIN'))
		])
class TransactionTax():
	tax_entity 
	
class Transaction ():
	BILL
	PURCHASE
	CREDIT_MEMO
	DEPOSIT
	ESTIMATE
	INVOICE
	JOURNAL_ENTRY
	REFUND_RECEPT
	SALES_RECEIPT
	TRANSFER
	VENDOR_CREDIT
	PURCHASE_ORDER
	
	
	category_name
	credit_account_name
	credit_account_amount = DecimalField(max_value=9, max_digits=2)
	debit_account_name
	debit_account_amount = DecimalField(max_value=9, max_digits=2)
	sales_discount=Integer (validators = [MaxValueValidator(100, message=values.get('SALES_DIS_MAX')),MinValueValidator(0, message= values.get('SALES_DIS_MIN'))])
	discount_period = IntegerField(validators = [MaxValueValidator(100, message=values.get('NetDue')),MinValueValidator(0, message= values.get('SALES_DIS_MIN'))])
	net_due = Integer(validators = [MaxValueValidator(100, message=values.get('SALES_DIS_MAX')),MinValueValidator(0, message= values.get('SALES_DIS_MIN'))])
	currency_ref = CharField(max_lenght=3,default="USD")

	sync_token  = CharField(max_length=40)
	total_amount = DecimalField(max_value=9, max_digits=2)
	state_tax_amount= DecimalField(max_value=9, max_digits=2)
	federal_tax_amount= DecimalField(max_value=9, max_digits=2)
	regulatory_tax_amount = DecimalField(max_value=9, max_digits=2)
	is_auto = BooleanField(default=False)
	frequency
	is_active = BooleanField(default=True)
	is_reoccuring = BooleanFiled(default=False)
{
  "QueryResponse": {
    "startPosition": 1, 
    "maxResults": 1, 
    "RecurringTransaction": [
      {
        "Bill": {
          "SyncToken": "0", 
          "domain": "QBO", 
          "RecurringInfo": {
            "Active": true, 
            "RecurType": "Automated", 
          "TotalAmt": 74.36, 
      
          "Id": "20", 
          "sparse": false, 
 
          "Line": [
            {
              "Description": "Monthly Phone Bill", 
              "DetailType": "AccountBasedExpenseLineDetail", 
              "LineNum": 1, 
              "Amount": 74.36, 
              "Id": "1", 
              "AccountBasedExpenseLineDetail": {
                "TaxCodeRef": {
                  "value": "NON"
                }, 
                "AccountRef": {
                  "name": "Utilities:Telephone", 
                  "value": "77"
                }, 
                "BillableStatus": "NotBillable"
              }
            }
          ], 
          "Balance": 74.36, 
          "SalesTermRef": {
            "value": "3"
          }, 
          "MetaData": {
            "CreateTime": "2019-02-17T15:27:25-08:00", 
            "LastUpdatedTime": "2020-07-05T01:19:13-07:00"
          }
        }
      }
    ]
  }, 
  "time": "2020-07-09T10:18:02.049-07:00"
}
