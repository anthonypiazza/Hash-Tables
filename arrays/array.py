# POLYA
# 1. Ask Q
# 2. Plan
# 3. Implement - WE ARE HERE

class DynamicArray:
    def __init__(self, capacity=8):
        self.count = 0
        self.capacity = capacity
        self.storage = [None] * capacity
    
    def append(self, value):
        if self.count >= self.capacity:
            self.resize_array()
        
        self.storage[self.count] = value
        self.count += 1

    def insert(self, value, index):
        if self.count >= self.capacity:
            self.resize_array()
        
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]
        
        self.storage[index] = value
        self.count += 1

    def remove(self, index):
        # Find index we want
        # Replace with next value and move down list till end
        # Subtract from count
        # Resize? NO       |      Return any values? YES
        value = self.storage[index]
        for i in range(index, self.count -1, 1):
            self.storage[i] = self.storage[i+1]
        
        self.count -= 1
        return value

    def print(self):
        for value in self.storage:
            print(value)

    def resize_array(self):
        self.capacity *= 2
        # allocating empty array with capacity double the previous
        new_storage = [None] * self.capacity
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        
        self.storage = new_storage

    def add_to_front(self, value):
        self.insert(value, 0)