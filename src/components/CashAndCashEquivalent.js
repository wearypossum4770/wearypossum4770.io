/**
 *
 * @param {number}
 * Restricted Cash:
 * 	1.	If restricted and Current "Current Asset".
 * 	2.	If restricted and Not Current "Noncurrent Asset".
 * 	3.	If not restricted is "Cash".
 * 	4. 	Restricted Cash and Investments (see Note) ......... $3,730,000
 * 		----------------------------------------------------------------
 * 		Note: Restricted Cash. DETAILED EXPLANATION.
 * Bank Overdrafts:
 * 	1. 	Determine if material, if material should report on face of balance sheet or in related notes section.
 * 	2.	report as accounts payable in current liabilities.
 * 	3.	If overdraft occurs in another account at same bank, offset cash.
 * Short-term Paper:
 * 	1.	If days_to_maturity is less than 90 classification "Cash Equivalent" else it will be Temporary Investment.
 * Postdated Checks:
 * 	1.	Treate and list as "Accounts Receivable".
 * Postage Stamps:
 * 	1.	Treated as "Office Supply" or "Prepaid Expense".
 * Travel Advances:
 * 	1.	Treat as "Travel Receivable" if deducted from employee's payroll.
 * 	2.	Treat as "Prepaid Travel" if not deducted from employee's payroll.
 * */
const CashEquivalents = props => {}

export default CashEquivalents

class CashAndCashEquivalent {
    constructor() {
        this.is_restricted = false
        this.temp_classification = false
        this.is_current_asset = true
        this.balance_sheet_classification = null
        this.classification = null
        this.is_payroll_deduction = null
        this.offset_cash = false
        this.account_receivable = null
        this.current_liability = null
        this.days_to_maturity = 0
        this.transaction_amount = 0
        this.cash_router(this.temp_classification)
        // end-of-constructor
    }
    //end-of-function
}
