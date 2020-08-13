class TreasuryStock {
    constructor() {
        this.account_type = 'contra_equity'
        this.asset_direction_change = 'decrease'
        this.liability_direction_change = null
        this.equity_direction_change = 'decrease'
        this.gain_or_loss = null /**cannot recognize gain or loss*/
    }
    repurchase_share() {}
}
