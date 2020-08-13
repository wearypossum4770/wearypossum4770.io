import React from 'react'

const CashFlowContainer = props => {
    return (
        <table>
            <tr>
                <td>Cash flows from operating activities</td>
            </tr>
            <tr>
                <td></td>
                <td>Net Income</td>
                <td> </td>
            </tr>
            <tr>
                <td>Cash flows from investing activities</td>
            </tr>

            <tr>
                <td>Cash flows from financing activities</td>
            </tr>
            <tr>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
        </table>
    )
}
export default CashFlowContainer

const display = {
    operating_activities: {
        title: 'Cash flows from operating activities',
        accounts: {
            net_income: null,
        },
    },
    investing_activities: {
        title: 'Cash flows from investing activities',
    },
    financing_activities: {
        title: 'Cash flows from financing activities',
    },
    net_cash: null,
    cash_balance_beginning: null,
    cash_balance_ending: null,
}
