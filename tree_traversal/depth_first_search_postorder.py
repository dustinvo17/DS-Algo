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


def dfs_postorder(node,list_node=[]):
  if node is not None:
    list_node = dfs_postorder(node.left,list_node)
    list_node = dfs_postorder(node.right,list_node)
    list_node.append(node.val)
  return list_node

      #    10
    #   8     12
    #  6 9    11 13
# list_node_v = dfs_postorder(root)
def dfs_postorder_iterative(node):
 
  stack =[node]
  stack2 = []
  list_node =[]
  while len(stack) > 0:
    out_node =  stack.pop()
    stack2.append(out_node)
    

    if out_node.right is not None:
      stack.append(out_node.right)
    if out_node.left is not None:
      stack.append(out_node.left)
  while len(stack2) > 0:
    out_node = stack2.pop()
    list_node.append(out_node.val)
  return list_node
list_node_v  = dfs_postorder_iterative(root)
# print(list_node_v)
assert list_node_v == [6,9,8,11,13,12,10]
print('successful traverse tree with dfs postorder')