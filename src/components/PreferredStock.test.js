//

;[
    {
        year_delcared: 2010,
        dividends_declared: 15000,
        preferred_stock: null,
        par_value: 100,
        share_price: function () {
            return this.par_value * this.interest_rate
        },
        bond_par_value: null,
        interest_rate: 0.1,
    },
    {
        year_delcared: 2011,
        dividends_declared: 5000,
        preferred_stock: null,
        par_value: 100,
        share_price: function () {
            return this.par_value * this.interest_rate
        },
        bond_par_value: null,
        interest_rate: 0.1,
    },
    {
        year_delcared: 2012,
        dividends_declared: 0,
        preferred_stock: null,
        par_value: 100,
        share_price: function () {
            return this.par_value * this.interest_rate
        },
        bond_par_value: null,
        interest_rate: 0.1,
    },
    {
        year_delcared: 2013,
        dividends_declared: 40000,
        cumulative_preferred_stock: null,
        non_cumulative_preferred_stock: null,
        par_value: 100,
        bond_par_value: null,
        interest_rate: 0.1,
        outsanding_shares: 1000,
        share_price: function () {
            return this.par_value * this.interest_rate
        },
        preferred_stocks_expense: function () {
            return (
                this.cumulative_preferred_stock +
                this.non_cumulative_preferred_stock
            )
        },
        preferred_stock_payable: function () {
            return this.dividends_declared - this.preferred_stocks_expense
        },
        common_stocks_expense: function () {
            return this.preferred_stock_payable
                ? this.dividends_declared - this.preferred_stock_payable
                : null
        },
    },
]
// noncumulative perferred & common stock
//~ interest_rate
//~ par_value = 100
//~ dividends_declared
