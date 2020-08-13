class CommonStock {
    //~ 1. ownership intrests in business.
    //~ 2. shareholders
    //~ 3. vote for board of directors.
    //~ 4. share in profit or losses (not always).
    //~ 5. asset (have priority in residual liquidation)
    //~ 6. pre-emptive right (if stock issued)

    constructor() {
        this.par_value = null
        this.shares_authorized = null
        this.shares_issued = null
        this.shares_outstanding = null
        this.treasury_shares = null
        this.sale_price = null
        this.debit_balance = null
        this.credit_balance = null
        this.appears_on_statement = ['balance_sheet']
        this.certificate_of_stock = null
        this.in_excess_of_par = null
        this.is_no_par = false
        //~ this.additional_paid_in_capital = null;
    }
    //	if !this.is_no_par {this.in_excess_of_par = null /**only allow cash and stock to change*/}
    delcareDividends() {}

    issue_stock() {
        in_excess_of_par
    }

    stock_purchase() {}
}
