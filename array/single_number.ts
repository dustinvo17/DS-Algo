function singleNumber(nums: number[]): number {
    let found = {}
    for(let num of nums) {
        if(!found[num]) found[num] = 1
        else found[num] += 1
    }
    for(let key of Object.keys(found)) {
        if(found[key] == 1) return parseInt(key)
    }
};