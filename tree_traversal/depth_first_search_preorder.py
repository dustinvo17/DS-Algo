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


def dfs_preorder_recursive(node,list_node=[]):
  if node is not None:
    list_node.append(node)
    list_node = dfs_preorder_recursive(node.left,list_node)
    list_node = dfs_preorder_recursive(node.right,list_node)
  return list_node


# use stack to keep track of right node and queue to keep track of left node.
def dfs_preorder_iterative(node):
  if not node:
      return None
  
  list_node = []

  stack = [node]
  while len(stack) > 0 :
    out_node = stack.pop()
    list_node.append(out_node)      
    if out_node.right is not  None:
      stack.append(out_node.right)
    if out_node.left is not None:
      stack.append(out_node.left)
 
  return list_node
# // TEST ITERATIVE 
# list_node = dfs_preorder_iterative(root)


# TEST RECURSIVE 
list_node = dfs_preorder_recursive(root)


list_node_val = []
for node in list_node:
  list_node_val.append(node.val)

print(list_node_val)  
    #     10
    #   8     12
    #  6 9    11 13

assert list_node_val == [10,8,6,9,12,11,13]

print('successfully traverse tree with dfs preorder')