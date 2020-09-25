def rotate(sll,n):
  current = sll.head
  prev = None
  i = 0
  while i < n:
    prev = current
    current = current.next
    i +=1
  sll.tail.next = sl.head
  prev.next = None
  sll.tail = prev
  sll.head = current
  return
def rotate_no_tail(sll,n):
  p = sll.head
  q = p
  count = 0
  while True:
    if count < n - 1:
      p = p.next
      count +=1
    if q.next is not None:
      q = q.next
    if q.next is None:
      new_head = p.next
      p.next = None
      q.next = sl.head
      sl.head = new_head
      break
  return   
          
class Node:
  def __init__(self,v):
    self.v = v
    self.next = None
class SL:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
  def add(self,v):
    new_node = Node(v)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.length +=1
  def print_all(self):
    current = self.head
    list_node_v = []
    while current is not None:
      print(current.v)
      list_node_v.append(current.v)
      current = current.next
    print(current)
    return list_node_v
sl = SL()
sl.add(1)
sl.add(2)
sl.add(3)
sl.add(4)
sl.add(5)
sl.add(6)
sl.print_all()
print('========')
rotate_no_tail(sl,4)
assert sl.print_all() == [5,6,1,2,3,4]