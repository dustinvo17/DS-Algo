# Given a singly linked list, determine if it is a palindrome.

# Example 1:

# Input: 1->2
# Output: false
# Example 2:

# Input: 1->2->2->1
# Output: true
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        if not head:
            return True
        if head.next is None:
            return True
        j = head
        ll = []
        while j:
            ll.append(j.val)
            j = j.next
        count = 0
        while count < len(ll) // 2:
            if ll[count] != ll[len(ll)- count - 1]:
                return False
            count += 1
        return True

