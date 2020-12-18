class Node:
    def __init__(self, v):
        self.val = v
        self.next = None


l1 = Node(-9)
l1.next = Node(3)

l2 = Node(5)
l2.next = Node(7)



def mergeTwoLists( l1, l2):
    p = l1
    q = l2
    if l1 is None and l2:
        return l2
    if l2 is None and l1:
        return l1
    if l1 is None and l2 is None:
        return None
    if p.val < q.val:
        current_node = p
        p = p.next
    else:
        current_node = q
        q = q.next
    head = current_node

    while p and q:
        
        if p.val < q.val:
            current_node.next = p
            p = p.next
        else:
            current_node.next = q
            q = q.next
        current_node = current_node.next

    if p is not None:
        while p:
            current_node.next = p
            p = p.next
            current_node = current_node.next
    if q is not None:
        while q:
         
            current_node.next = q
            q = q.next
            current_node = current_node.next 
    return head

head = mergeTwoLists(l1,l2)
list_node = []
while head:
    list_node.append(head.val)
    head = head.next
assert list_node == [-9,3,5,7]

