function containsDuplicate(nums: number[]): boolean {
    let hash_map = {}
    for(let i = 0 ; i < nums.length; i++) {
        if(hash_map[nums[i]]){
            return true
        }else {
            hash_map[nums[i]] = true
        }
    }
    return false
};

function containsDuplicateWithSet(nums: number[]): boolean {
    return (new Set(nums)).size !== nums.length
};