class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        """Check if the linked list is empty"""
        return self.head is None
    
    def length(self):
        """Return the length of the linked list"""
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
          self.head = new_node
        else:
          new_node.next = self.head
          self.head = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
    
    def insert_at_position(self, data, position):
        """Insert a new node at the specified position (0-based index)"""
        if position < 0 or position > self.length():
            raise IndexError("Invalid position")
        
        if position == 0:
            self.insert_at_beginning(data)
        else:
            new_node = Node(data)
            previous = self.head
            current = self.head
            for _ in range(position - 1):
                previous = current
                current = current.next
            previous.next = new_node
            new_node.next = current
    
    def delete_from_beginning(self):
        if self.is_empty():
            raise Exception("List is empty")
        self.head = self.head.next
    
    def delete_from_end(self):
        if self.is_empty():
            raise Exception("List is empty")
        
        if self.head.next is None: #single node deletion
            self.head = None
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None
    
    def delete_from_position(self, position):
        """Delete the node at the specified position (0-based index)"""
        if position < 0 or position >= self.length():
            raise IndexError("Invalid position")
        
        if position == 0:
            self.delete_from_beginning()
        else:
            previous = self.head
            current = self.head
            for _ in range(position - 1):
                previous = current
                current = current.next
            previous.next = current.next
    
    def search(self, data):
        """Search for a node with the given data"""
        current = self.head
        position = 0
        while current is not None:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

    def display(self):
        """Display the linked list"""
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
            
        print("NULL")
    
    def clear(self):
        """Clear the entire linked list"""
        self.head = None


# Example usage
if __name__ == "__main__":
    sll = SinglyLinkedList()
    n = int(input())
    for _ in range(n):
      value = int(input())
      sll.insert_at_end(value)
    
    print("Insert elements at Last")  
    sll.display()
    
    value = int(input())
    pos = int(input())
    print("Insert", value, "at", pos, "position")
    sll.insert_at_position(value, pos)
    sll.display()
    
    value = int(input())
    print("Insert element at beginning")
    sll.insert_at_beginning(value)
    sll.display()
    
    print("Delete Last element")
    sll.delete_from_end()
    sll.display()    
    
    print("Delete First element")
    sll.delete_from_beginning()
    sll.display()
    
    pos = int(input())
    print("Delete element at", pos, "position")
    sll.delete_from_position(pos)
    sll.display()
    
    print("Length of linked list", sll.length())
    key = int(input())
    found = sll.search(key)
    if found == -1:
      print(key,"is not found in the list")
    else:
      print(key,"is found at",found,"position in the list")
    
    #print(n)
    #sll.display()