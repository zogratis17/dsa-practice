class MyCircularQueue:
    def __init__(self, k):
        self.k = k
        self.a = [0] * k
        self.head = 0
        self.size = 0

    def enQueue(self, value):
        if self.isFull():
            return False
        tail = (self.head + self.size) % self.k
        self.a[tail] = value
        self.size += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.k
        self.size -= 1
        return True

    def Front(self):
        return -1 if self.isEmpty() else self.a[self.head]

    def Rear(self):
        if self.isEmpty():
            return -1
        tail = (self.head + self.size - 1) % self.k
        return self.a[tail]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.k


k = int(input())   # queue size
q = int(input())   # number of operations

cq = MyCircularQueue(k)

for _ in range(q):
    parts = input().split()
    op = parts[0]

    if op == "enQueue":
        print(cq.enQueue(int(parts[1])))
    elif op == "deQueue":
        print(cq.deQueue())
    elif op == "Front":
        print(cq.Front())
    elif op == "Rear":
        print(cq.Rear())
    elif op == "isEmpty":
        print(cq.isEmpty())
    elif op == "isFull":
        print(cq.isFull())
