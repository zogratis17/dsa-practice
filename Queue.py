class Queue:
    def __init__(self):
        self.items = []
        self.ptr = -1

    def enqueue(self, item):
        self.items.append(item)
        self.ptr += 1

    def dequeue(self):
        if self.ptr == -1:
            return None
        item = self.items.pop(0)
        self.ptr -= 1
        return item

    def is_empty(self):
        return self.ptr == -1

    def peek(self):
        if self.ptr == -1:
            return None
        return self.items[0]

q = Queue()
while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Is Empty")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        item = input("Enter item to enqueue: ")
        q.enqueue(item)
    elif choice == "2":
        item = q.dequeue()
        if item is not None:
            print("Dequeued:", item)
        else:
            print("Queue is empty")
    elif choice == "3":
        item = q.peek()
        if item is not None:
            print("Front item:", item)
        else:
            print("Queue is empty")
    elif choice == "4":
        if q.is_empty():
            print("Queue is empty")
        else:
            print("Queue is not empty")
    elif choice == "5":
        break
    else:
        print("Invalid choice")