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
    print(f"Printing the list now, starting with current at {self.current}")
    print(self.storage)
    buffer_list = []
    append_index = self.current
    for i in range(0, len(self.storage)):
      print(f"current is {self.current}")
      if append_index >= len(self.storage) -1:
        append_index = 0
      else:
        append_index += 1
      if self.storage[append_index]:
        print(f"Current is {append_index}, appending {self.storage[append_index]}")
        buffer_list.append(self.storage[append_index])
    print(f"finished printing with current at {append_index}")

    return buffer_list
