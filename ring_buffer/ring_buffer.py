class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current > len(self.storage) - 1:
      self.current = 0 #If current has hit the end of the array, send it back to beginning
    
    self.storage[self.current] = item
    self.current += 1



  def get(self):
    rtn_list = []
    for i in range(0, len(self.storage)):
      if self.storage[i]:
        rtn_list.append(self.storage[i])
    return rtn_list
