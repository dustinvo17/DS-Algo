// Reverse a singly linked list.

// Example:

// Input: 1->2->3->4->5->NULL
// Output: 5->4->3->2->1->NULL
// Follow up:

// A linked list can be reversed either iteratively or recursively. Could you implement both?Reverse a singly linked list.

// Example:

// Input: 1->2->3->4->5->NULL
// Output: 5->4->3->2->1->NULL
// Follow up:

// A linked list can be reversed either iteratively or recursively. Could you implement both?

/** null-1 
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

function reverseList(head: ListNode | null): ListNode | null {
    let prev = null
    let cur = head
    while(cur){
        let temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    }
    head = prev
    return head
};
// recursion 

function reverseListRecursion(head: ListNode | null): ListNode | null {
    
    return traverse(null, head)
};
function traverse(prev: ListNode | null ,cur: ListNode | null) {
        if(!cur) return prev
          let temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
     return traverse(prev,cur)
}