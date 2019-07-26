class Binary_Search_Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if value <= self.value:
            if self.left:
                self.left.add(value)
            else:
                self.left = Binary_Search_Tree(value)
        elif value > self.value:
            if self.right:
                self.right.add(value)
            else:
                self.right = Binary_Search_Tree(value)

    def search(self, value):
        if self.value == value:
            return True
        elif value <= self.value:
            if not self.left:
                return False
            else:
                return self.left.search(value)
        else:
            if not self.right:
                return False
            else:
                return self.right.search(value)

    