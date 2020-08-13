import React from 'react'
import {current_assets} from './test_current_assets.js'
import {currencyFormat} from '../contrib/helpers.js'
const render_balance = function () {
    const render_elements = []
    current_assets.sub_accounts.forEach(account =>
        render_elements.push(
            <tr>
                <td></td>
                <td style={{textAlign: 'left'}}>{account.account_name}</td>
                <td style={{textAlign: 'right'}}>
                    {currencyFormat.format(account.account_balance)}
                </td>
                <td></td>
            </tr>
        )
    )
    render_elements.push(
        <tr>
            <td colSpan='4' style={{textAlign: 'right'}}>
                <u>{currencyFormat.format(current_assets.balance())}</u>
            </td>
        </tr>
    )
    return render_elements
}

const CurrentAssets = props => {
    return (
        <table>
            <tbody>
                <tr>
                    <td colSpan='4' style={{textAlign: 'left'}}>
                        Receivables
                    </td>
                </tr>
                {render_balance()}
            </tbody>
        </table>
    )
}
export default CurrentAssets
