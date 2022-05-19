function checkCashRegister(price, cash, cid)
{
    const unitAmount = 
    {
        "PENNY":          0.01,
        "NICKEL":         0.05,
        "DIME":           0.10,
        "QUARTER":        0.25,
        "ONE":            1.00,
        "FIVE":           5.00,
        "TEN":            10.00,
        "TWENTY":         20.00,
        "ONE HUNDRED":    100.00
    };

    const change = [];
    const totalCID = cid.reduce(
        (accumulator, value) => accumulator + value[1],
        0).toFixed(2);

    let remainingAmount = cash - price;
    
    if (remainingAmount > totalCID) 
    {
        return { status: "INSUFFICIENT_FUNDS", change };
    } 
    else if (remainingAmount.toFixed(2) === totalCID)
    {
        return { status: "CLOSED", change: cid };
    } 
    
    cid = cid.reverse().forEach(item => {
        const itemName  = item[0];
        const temporary = [itemName, 0];

        while (remainingAmount >= unitAmount[itemName] && item[1] > 0)
        {
            temporary[1]      += unitAmount[itemName];
            item[1]           -= unitAmount[itemName];

            remainingAmount   -= unitAmount[itemName];
            remainingAmount    = remainingAmount.toFixed(2);
        }

        if (temporary[1] > 0) change.push(temporary);
    });

    if (remainingAmount > 0) 
    {
        return { status: "INSUFFICIENT_FUNDS", change: [] };
    }

    return { status: "OPEN", change };
}

checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);