

class Stack:

    def __init__(self, items = [], limit = 100):
        self.items =  items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.full():
            print('stack is full')
        else:
            self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.items.pop()

    def peek(self):
        index = len(self.items) - 1
        return self.items[index]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        index = None

        for i, item in enumerate(self.items):
            if item == target:
                index = i
                break
        
        if index == None:
            return -1
        elif index == len(self.items) - 1:
            return 0
        else:
            reversed_index = len(self.items) - 1 - index
            return reversed_index
        
            





