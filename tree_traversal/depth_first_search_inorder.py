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


def dfs_inorder(node,list_node=[]):
  if node is not None:
    
    list_node = dfs_inorder(node.left,list_node)
    list_node.append(node.val)
    list_node = dfs_inorder(node.right,list_node)
  return list_node

def dfs_inorder_iterative(node):
  s = []
  current_node = node
  list_node_v = []
  while current_node is not None:
    s.append(current_node)
    current_node = current_node.left
  while len(s) >0:
    print(node.val)
    out_node = s.pop()
    list_node_v.append(out_node.val)
    print(out_node.val)
    out_node = out_node.right
    while out_node is not None:
      s.append(out_node)
      out_node = out_node.left
  return list_node_v


assert dfs_inorder_iterative(root)  == [6,8,9,10,11,12,13]
assert dfs_inorder(root) == [6,8,9,10,11,12,13]
print('succesfully traverse tree with dfs')