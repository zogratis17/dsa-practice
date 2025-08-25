class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.length += 1

    def __str__(self):
        parts = []
        curr = self.head
        while curr:
            if isinstance(curr.data, float) and curr.data.is_integer():
                parts.append(str(int(curr.data)))
            else:
                parts.append(str(curr.data))
            curr = curr.next
        return " <-> ".join(parts) + " <-> NULL"

def create_doubly_linked_list(values):
    dll = DoublyLinkedList()
    for v in values:
        dll.append(v)
    return dll

n = int(input().strip())
vals = []
for _ in range(n):
    s = input().strip()
    try:
        iv = int(s)
        vals.append(iv)
    except ValueError:
        vals.append(float(s))

dll = create_doubly_linked_list(vals)
print(n)
print(dll)
