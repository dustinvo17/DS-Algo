class Node:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

root = Node(10)
root.left = Node(8)
root.left.left = Node(6)
root.left.right = Node(9)
root.right = Node(12)
root.right.left = Node(11)
root.right.right = Node(13)
    #     10
    #   8     12
    #  6 9    11 13

def validate(node,min,max):
  if not node:
    return True
  if max is not None and node.val > max:
    return False
  if min is not None and node.val < min:
    return False
  return validate(node.left,min,node.val) and validate(node.right,node.val,max)
print(validate(root,None,None))