class max_binary_heap:
  def __init__(self):
    self.values = []
  def insert_heap(self,val):
  
    heap = self.values
    heap.append(val)
      # BUBLE UP UNTIL MEET RIGHT SPOT
    current_index = len(heap) - 1
    parent_index = (current_index -1) // 2
    while heap[current_index] > heap[parent_index] and current_index > 0: 
      heap[current_index],heap[parent_index] = heap[parent_index],heap[current_index]
      current_index = parent_index  
      parent_index = (current_index -1) // 2
    return heap

  def extract_max(self):
    heap = self.values
    current_index = 0
    heap[current_index] = heap[len(heap) - 1]
    # CHANGE FIRST INDEX VALUE INTO LAST INDEX VALUE
    removed_node = heap.pop()
    # POP LAST ELEM WHICH IS THE LARGEST NODE

    # SINK DOWN THE CURRENT NODE , SWAP WITH THE LARGEST CHILD THAT'S GREATER THAN IT
    while True:
      left_child_index = (current_index * 2) + 1
      if left_child_index >= len(heap)-1:
        # AT THE END AND 
          if left_child_index == len(heap) -1 and heap[left_child_index] > heap[current_index]:
            heap[current_index],heap[left_child_index] = heap[left_child_index],heap[current_index]
          break
      right_child_index = left_child_index + 1
      
      if heap[current_index] > heap[left_child_index] and heap[current_index] > heap[right_child_index]:
        # CORRECT SPOT
        break
      # FIND LARGEST CHILD INDEX 
      largest_child_index = left_child_index if max(heap[left_child_index],heap[right_child_index]) == heap[left_child_index] else right_child_index
      heap[current_index],heap[largest_child_index] = heap[largest_child_index],heap[current_index]
      current_index = largest_child_index
      
    return removed_node

mb_heap = max_binary_heap()
mb_heap.insert_heap(41)
mb_heap.insert_heap(39)
mb_heap.insert_heap(33)
mb_heap.insert_heap(18)
#      41
#     /  \
#   39   33
#   / 
# 18
#  
assert mb_heap.values == [41,39,33,18]

mb_heap.insert_heap(44)
#      44
#     /  \
#   41   33
#   / \
#  18 39
assert mb_heap.values == [44,41,33,18,39]
mb_heap.insert_heap(100)
#    100
#   /   \
#  41    44
# / \    /
# 18 39  33
assert mb_heap.values == [100,41,44,18,39,33]

mb_heap.extract_max()

#    44
#   /   \
#  41    33
# / \    
# 18 39  
assert mb_heap.values == [44,41,33,18,39]
mb_heap.extract_max()

#    41
#   /   \
#  39    33
# /   
# 18 
assert mb_heap.values == [41,39,33,18]  
#    41
#   /   \
#  39    33
# /  \ 
# 18  17
mb_heap.values.append(17)
mb_heap.extract_max()
print(mb_heap.values)
#    39
#   /   \
#  18    33
# /   
# 17
assert mb_heap.values == [39,18,33,17]

