function maxProfit(prices: number[]): number { 
    if(!prices || prices.length == 0){
        return 0
    }
    let profit = 0
    for(let i = 0; i < prices.length - 1; i++) {
        const buy = prices[i]
        const sell = prices[i+1]
        if(sell > buy) {
            profit += (sell - buy)
        }
    }
    return profit
};