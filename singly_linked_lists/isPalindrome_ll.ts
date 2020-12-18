// Given a singly linked list, determine if it is a palindrome.

// Example 1:

// Input: 1->2
// Output: false
// Example 2:

// Input: 1->2->2->1
// Output: true
// Follow up:
// Could you do it in O(n) time and O(1) spa
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */        
function isPalindrome(head: ListNode | null): boolean {
    if(!head) return true
    let stack = []
    let queue = []
    let cur = head
    while(cur) {
        stack.push(cur.val)
        queue.push(cur.val)
        cur = cur.next
    }
    while(stack.length > 0 || queue.length > 0){
        if(stack.pop() !== queue.shift()){
            return false
        }
    }
    if(stack.length > 0 || queue.length > 0) return false
    return true
   
    
};
function isPalindrome2P(head: ListNode | null): boolean {
    if(!head) return true
    let slow = head
    let fast = head
    while(fast.next && fast.next.next) {
        slow = slow.next
        fast = fast.next.next
    }
    let prev = null
    while(slow) {
        let temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
        
    }
    let start = head
    let end = prev
    while(end && start){
        if(start.val !== end.val) return false
        start = start.next
        end = end.next
    }
    return true
   
    
};