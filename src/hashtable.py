# '''
# Linked List hash table key/value pair
# '''

# Hash Collision - when a key hashes to the same value
# Hash functions are psuedo random 
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.
        # Print a warning
        Hash collisions should be handled with Linked List Chaining.
        Fill this in.
        '''
        index = self._hash_mod(key)

        if(self.storage[index]):
            # print("\n\nHash collisions should be handled with Linked List Chaining.")
            current_list_node = self.storage[index]
            while current_list_node.next:
                if current_list_node.key == key:
                    current_list_node.value = value
                    break
                else:
                    current_list_node = current_list_node.next
            if current_list_node.key == key:
                current_list_node.value = value
            else:        
                current_list_node.next = LinkedPair(key, value)
            # print(f"Index: {index}, cuurent list node Ending: {current_list_node.value}, Current List Node Ending Next:{current_list_node.next.value}\n\n")
        
        else:
            self.storage[index] = LinkedPair(key, value)
            # print(f"Index: {index}, cuurent list node: {self.storage[index].value}")   


    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''
        index = self._hash_mod(key)

        current_list_node = self.storage[index]
        
        if current_list_node.next:
            while current_list_node.next:
                if current_list_node.key == key:
                    # print(f"Current List Node: {current_list_node.value}")
                    current_list_node.value = None
                    # print(f"Current List Node: {current_list_node.value}")
                    break
                else:
                    current_list_node = current_list_node.next
            if current_list_node.key == key:
                # print(f"Current List Node: {current_list_node.value}")
                current_list_node.value = None
                # print(f"Current List Node: {current_list_node.value}") 
        
        else:
            # print(f"Current List Node: {current_list_node.value}")
            current_list_node.value = None
            # print(f"Current List Node: {current_list_node.value}")

            # if current_list_node.key == key:
            #         current_list_node = None
            # print('Key is not found')



    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        index = self._hash_mod(key)

        if(self.storage[index]):
            current_list_node = self.storage[index]
            
            if current_list_node.next:
                while current_list_node.next:
                    # print(f'Hiiii {key}')
                    if current_list_node.key == key:
                        # print(f'Hiii {key}')
                        return current_list_node.value
                    else:
                        current_list_node = current_list_node.next
                
                if current_list_node.key == key:
                    # print(f'Hii {key}')
                    return current_list_node.value
                
                else:
                    # print(f'Hi {key}')
                    return None
            
            else:
                # print(f'Hiiiii {key}')
                return current_list_node.value

        else:
            # print(f'Hiiiii {key}')
            # print(None)
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        # Hash table is dynamice array
        Fill this in.
        '''
        self.capacity = self.capacity*2
        new_storage = [index for index in self.storage]
        self.storage = [None] * self.capacity

        # print(new_storage)
        for i in range(0, len(new_storage)):
            # print(i)
            current_list_node = new_storage[i]
            if current_list_node == None:
                pass
            elif current_list_node.next:
                while current_list_node.next:
                    self.insert(current_list_node.key, current_list_node.value)
                    current_list_node = current_list_node.next
                self.insert(current_list_node.key, current_list_node.value)
            else:
                self.insert(current_list_node.key, current_list_node.value)
                




if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
