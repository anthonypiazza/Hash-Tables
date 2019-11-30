import this

this

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node

class LinkedList:
    def __init__(self, set_head=None):
        self.head = set_head
    
    def add_to_head(self, value):
        # Create a head node
        new_node = Node(value, self.head)
        # Set current head to new_node
        self.head = new_node
    
    def remove(self, value):
        # Find and remove the node with the given value
        #If we have no head:
        if not self.head:
            # print an error and return
            print("Error: Value not found")
        #if the head has our value:
        elif self.head.value == value:
            # remove the head by pointing self.head to self.next
            self.head = self.head.next
        #else:
        else:
            # keep track of the parent node
            parent = self.head
            current = self.head.next
            # Walk through the linked list until we find a matching value
            while current:
                # If we find a matching value
                if current.value == value:
                    # point parent.next to node.next
                    parent.next = current.next
                    return
            # If we get to the end and have not found the value, print error
            print("Error: Value not found")

    def contains(self, value):
        # return True if LL contains the value
        # return False if it does not
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False 

    def print(self):
        current = self.head
        linked_list_string = ""
        while current:
            linked_list_string += f"{current.value}"
            current = current.next
            linked_list_string += " --> "
        linked_list_string += "None"
        print(linked_list_string)  


ll = LinkedList()
ll.add_to_head(1)
ll.add_to_head(2)
ll.add_to_head(3)
print(ll.contains(2)) #True
ll.remove(2)
print(ll.contains(2)) #False