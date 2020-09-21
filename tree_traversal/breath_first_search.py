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


def bfs_iterative(node):
  queue = [node]
  list_node = []
  while len(queue) > 0:
    first_out_node = queue.pop(0)
    list_node.append(first_out_node)
    if first_out_node.left is not None:
      queue.append(first_out_node.left)
    if first_out_node.right is not None:
      queue.append(first_out_node.right)
  return list_node

list_node_return = bfs_iterative(root)
list_node_val = []
for node in list_node_return:
  print(node.val)
  list_node_val.append(node.val)
assert list_node_val == [10,8,12,6,9,11,13]
print('traverse tree with bfs successfully ')

