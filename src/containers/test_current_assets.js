import React from 'react'
export const current_assets = {
    has_sub_accounts: true,
    account_type: 'current assets',
    account_name: 'Receivables',
    sub_accounts: [
        {
            account_name: 'Trade',
            account_balance: 251005,
            increase_in_asset: true,
        },
        {
            account_name: 'Due from Foreign Affiliates',
            account_balance: 90019,
            increase_in_asset: true,
        },
        {
            account_name: 'Other',
            account_balance: 26349,
            increase_in_asset: true,
        },
    ],
    balance: function () {
        let trial_balance = []
        this.sub_accounts.forEach(element =>
            trial_balance.push(element.account_balance)
        )
        return trial_balance.reduce((accum, currVal) => accum + currVal)
    },
}
