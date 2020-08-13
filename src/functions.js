const account_type_enumeration = [
    'asset',
    'contra_asset',
    'liability',
    'contra_liability',
    'equity',
    'contra_equity',
]
const original_cost = 0
const accumulated_depreciation = 0
const proceeds_from_sale = 0

const net_book_value = original_cost - accumulated_depreciation
const gain_or_loss = proceeds_from_sale - net_book_value

const paid_in_capital = {
    common_stock: {
        par_value: null,
        oustanding_shares: null,
        sale_price: null,
        debit_balance: null,
        credit_balance: null,
        appears_on_statement: null,
    },
    //~ preferred_stock:null,
    in_excess_of_par: null,
}
