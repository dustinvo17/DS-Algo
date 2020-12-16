function reverse(x: number): number {
    var min = Math.pow(-2, 31)
    var max = Math.pow(2, 31)
    var result: any = ''
    var x_string = Math.abs(x).toString()
    for (let char of x_string) {
        result = char + result
    }
    if (x >= 0) result = parseInt(result) * 1
    else result = parseInt(result) * -1
    var condition = result > min && result < max
    return condition ? result : 0

};
function reverseMath(x: number): number {
    const isNegative = x < 0;
    x = Math.abs(x);
    let ret = 0;
    while (x > 0) {
        const num = x % 10;
        x = Math.floor(x / 10);
        ret *= 10;
        ret += num;
    }
    if (ret > Math.pow(2, 31)) return 0;
    return isNegative ? ret * -1 : ret;
};
