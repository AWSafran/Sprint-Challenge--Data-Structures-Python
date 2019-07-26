class Binary_Array:
    def __init__(self, len):
        self.storage = [None] * (len * 2) # a good start to making sure we have enough indexes, but probably won't be enough to cover it

    def find_child(self, value, index):
        if value > self.storage[index]:
            child_index = index * 2 + 2
        else: 
            child_index = index * 2 + 1
        return child_index

    def add(self, value, index=0):
        if self.storage[index] is None: # Need this for first time adding
            print("adding first value")
            self.storage[index] = value
            return
        if value == self.storage[index]:
            print("Value already in list, don't need to add")
            return #It's already in here

        child_index = self.find_child(value, index)

        while len(self.storage) < child_index + 1:
            array_to_concat = [None] * index
            self.storage.extend(array_to_concat) #Make sure we have children to compare to. We can't just add 'None' once because of the index arithmetic


        if self.storage[child_index] is None:
            self.storage[child_index] = value
            return
        else:

            self.add(value, child_index)
    
    def search(self, value, index=0):
        if self.storage[index] == value:
            return True

        child_index = self.find_child(value, index)

        if self.storage[child_index] is None:
            return False
        
        else:
            return self.search(value, child_index)
        

    
