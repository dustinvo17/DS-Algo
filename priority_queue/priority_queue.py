class Node:
  def __init__(self,v,p):
    self.v = v  # v =  value
    self.p = p  # p = priority
class priority_queue:
  def __init__(self):
    self.nodes = []
  def enqueue(self,v,p):
    new_node = Node(v,p)
    nodes = self.nodes
    nodes.append(new_node)
    current_index = len(nodes) - 1
    while True:
      parent_index = (current_index - 1) // 2 
      if parent_index < 0:
        break
      parent_node = nodes[parent_index]
      current_node = nodes[current_index]
      if parent_node.p <  current_node.p:
        break
      nodes[parent_index], nodes[current_index]= nodes[current_index],nodes[parent_index]
      current_index = parent_index
    return nodes
  def dequeue(self):
    nodes = self.nodes
    current_index = 0
    nodes[current_index] = nodes[len(nodes)-1]
    nodes.pop()
    # swap top priority to the bottom and remove it
    while True:
      left_i = current_index * 2  + 1
      if left_i >= len(nodes) -1:
        if left_i == len(nodes) - 1:
          # when left_i is the index of last element in the queue
          if nodes[current_index].p > nodes[left_i].p:
            nodes[current_index],nodes[left_i] = nodes[left_i], nodes[current_index]
        break
      right_i = left_i + 1
      left_child_p = nodes[left_i].p
      right_child_p = nodes[right_i].p
      current_node_p = nodes[current_index].p
      if left_child_p > current_node_p and right_child_p > current_node_p:
        break
      smallest_child_p_i = left_i if min(left_child_p,right_child_p) == left_child_p else right_i
      nodes[current_index],nodes[smallest_child_p_i] = nodes[smallest_child_p_i],nodes[current_index]
      current_index = smallest_child_p_i
    return
pq = priority_queue()
n1 = Node(4,4)
n2 = Node(5,5)
n3 = Node(6,6)
pq.nodes.append(n1)
pq.nodes.append(n2)
pq.nodes.append(n3)
pq.enqueue(3,3)
pq.enqueue(8,8)
pq.enqueue(1,1)

def add_node_v(pq):
  list_nodes = []
  for node in pq.nodes:
  
    list_nodes.append(node.v)
  return list_nodes

list_nodes =  add_node_v(pq)

#    1
#  /  \
# 4     3
# /\   /
# 5 8  6
assert list_nodes == [1,4,3,5,8,6]
pq.dequeue()

list_nodes = add_node_v(pq)

assert list_nodes == [3,4,6,5,8]
#    3
#  /  \
# 4     6
# /\   /
# 5 8  
pq.dequeue()

#    4
#  /  \
# 5     6
# /  
# 8
list_nodes = add_node_v(pq)
assert list_nodes == [4,5,6,8]  


