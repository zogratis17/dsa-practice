class Stack:
    def __init__(self, max_size=100):
        self.stack = [0] * max_size
        self.top = -1
        self.max_size = max_size

    def push(self, data):
        if self.top >= self.max_size - 1:
            print('Stack overflow! Cannot push element.')
            return
        self.top += 1
        self.stack[self.top] = data
        print(f'{data} pushed to stack')

    def pop(self):
        if self.is_empty():
            print('Stack underflow! Cannot pop element.')
            return None
        data = self.stack[self.top]
        self.top -= 1
        print(f'{data} popped from stack')
        return data

    def peek(self):
        if self.is_empty():
            print('Stack is empty.')
            return None
        print(f'Top element is {self.stack[self.top]}')
        return self.stack[self.top]
    
    def is_empty(self):
        return self.top == -1
    
    def is_empty_print(self):
        if self.is_empty():
            print('Stack is empty.')
        else:
            print('Stack is not empty.')
    
    def display(self):
        if self.is_empty():
            print('Stack is empty.')
            return
        for i in range(self.top+1):
            print(self.stack[i], end=' ')
        print()

stack = Stack()

while True:
    op = int(input())
    if op == 1: 
        value = int(input())
        stack.push(value)
    
    elif op == 2: 
        stack.pop()
    
    elif op == 3: 
        stack.peek()
    
    elif op == 4: 
        stack.is_empty_print()

    elif op == 5:
        stack.display()
    
    elif op == 6: 
        print("Exiting...")
        break
    
    else:
        print("Invalid choice.")
