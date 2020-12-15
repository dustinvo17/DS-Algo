// Given an array, rotate the array to the right by k steps, where k is non-negative.

// Follow up:

// Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
// Could you do it in-place with O(1) extra space?
 
// Example 1:

// Input: nums = [1,2,3,4,5,6,7], k = 3
// Output: [5,6,7,1,2,3,4]
// Explanation:
// rotate 1 steps to the right: [7,1,2,3,4,5,6]
// rotate 2 steps to the right: [6,7,1,2,3,4,5]
// rotate 3 steps to the right: [5,6,7,1,2,3,4]

// Example 2:

// Input: nums = [-1,-100,3,99], k = 2
// Output: [3,99,-1,-100]
// Explanation: 
// rotate 1 steps to the right: [99,-1,-100,3]
// rotate 2 steps to the right: [3,99,-1,-100]
function rotate(nums: number[], k: number): void {
    for(let i = 0 ; i < k ; i++) {
        let elem = nums.pop()
        nums.unshift(elem)
    }
    
};
// optimoal 

function rotate_optimal(nums: number[], k: number):void {
    let new_array = new Array(nums.length)
    for(let i = 0; i < nums.length; i++) {
        new_array[(i + k) % nums.length] = nums[i]
    }
    for(let i = 0; i < nums.length; i++) {
        nums[i] = new_array[i]
    }
}
// 
function rotate_optimal_reverse(nums: number[], k: number):void {
    k = k % nums.length
    reverse(nums,0,nums.length - 1)
    reverse(nums,0,k-1)
    reverse(nums,k,nums.length - 1)
}

function reverse(nums:number[],start:number,end:number) {
    while(start < end){
        const temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start +=1
        end -= 1
    }
}
