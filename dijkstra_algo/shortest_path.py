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
    nodes[current_index], nodes[len(nodes)-1] = nodes[len(nodes)-1],nodes[current_index]
    out_node =nodes.pop()
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
    return out_node
class Edge:
  def __init__(self,node,weight):
    self.node = node
    self.weight = weight
weighted_graph ={
  "A": [Edge("B",4), Edge("C",2)],
  "B":[Edge("A",4),Edge("E",3)],
  "C":[Edge("A",2),Edge("D",2),Edge("F",4)],
  "D":[Edge("C",2),Edge("E",3),Edge("F",1)],
  "E":[Edge("B",3),Edge("D",3),Edge("F",1)],
  "F":[Edge("C",4),Edge("D",1),Edge("E",1)]
}

 
def shortest_path(start,end):
  distances = {}
  p_q = priority_queue()

  prev = {}
  for vertex in weighted_graph.keys():
    distances[vertex] = float('inf') if vertex != start else 0
    prev[vertex] = None
    priority = float('inf') if vertex != start else 0
    p_q.enqueue(vertex,priority)
  visited = {}
  print(distances)
  print(prev)
  
  while len(p_q.nodes) > 0:
    smallest = p_q.dequeue().v
    adj_list = weighted_graph[smallest]
    for neighbor in adj_list:
      candidate = distances[smallest] + neighbor.weight
      if candidate < distances[neighbor.node]:
        distances[neighbor.node] = candidate
        prev[neighbor.node] = smallest
        p_q.enqueue(neighbor.node,candidate)
  
  
shortest_path("A","E")