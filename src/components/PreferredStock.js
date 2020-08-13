class PreferredStock {
    //~ converible callable
    //~ 1. cumulative (paid before common)
    //~ 2. participating (threshold dividends on common share, if exceeds threshold, then preferred share in dividend)
    //~ 3. convertiable (1 share p/s => 15 shares of c/s)
    //~ 4. callable (right of repurchase => transfer to treasury stock)
    //~ 5. redemable (must pay at end of time frame, cannot repurchase)
    //~ 6. non-voting (can vote, have ownership)
    //~ 7. dividends payments or not tax deductible
    constructor() {
        this.last_issue = null
        this.stock_balance = null
        this.common_stock_threshold = null
        this.is_cumulative = false
        this.is_participating = false
        this.is_convertiable = false
        this.is_callable = false
        this.is_redeemable = false
        this.is_voting = false

        this.dividens_in_arrears = null

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

        //~ this.additional_paid_in_capital= null;
    }
    costOfStock() {
        const net_proceeds_per_share =
            market_price_per_share - floatation_cost_per_share
        return flotation_cost_incurred
            ? anual_dividend / net_proceeds_per_share
            : annual_dividend / market_price_per_share
    }
    delcareDividends() {}
    issue_stock() {
        in_excess_of_par
    }
    stock_purchase() {}
}
