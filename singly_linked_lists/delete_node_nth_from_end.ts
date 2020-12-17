// Given the head of a linked list, remove the nth node from the end of the list and return its head.

// Follow up: Could you do this in one pass?

 

// Example 1:

// Input: head = [1,2,3,4,5], n = 2
// Output: [1,2,3,5]
// Example 2:

// Input: head = [1], n = 1
// Output: []
// Example 3:

// Input: head = [1,2], n = 1
// Output: [1]
 

// Constraints:

// The number of nodes in the list is sz.
// 1 <= sz <= 30
// 0 <= Node.val <= 100
// 1 <= n <= sz

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    if(!head || head.next == null && n > 0){
        head = null
        return head
    }
    let dummy = new ListNode(0)
    dummy.next = head
    var length = 1
    let current = head
    while(current.next) {
        current = current.next
        length += 1
    }
    length = length - n  
    current = dummy
    while(length > 0) {
        current = current.next
        length -= 1
    }
    current.next = current.next.next
    return dummy.next
    
};
function twopointer_removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    let dummy = new ListNode(0)
    dummy.next = head
    let fast = dummy
    let slow = dummy
    let counter = 0
    while(counter < n) {
        fast = fast.next
        counter +=1
    }
    while(fast.next) {
        slow = slow.next
        fast = fast.next
    }
    slow.next = slow.next.next
    return dummy.next
};