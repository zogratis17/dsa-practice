class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"{data} pushed to stack")

    def pop(self):
        if self.is_empty():
            print("Stack underflow! Cannot pop")
        else:
            popped = self.top.data
            self.top = self.top.next
            print(f"Popped element is {popped}")

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print(f"Top element is {self.top.data}")

    def is_empty(self):
        return self.top is None

stack = Stack()
while True:
  try:
      choice = int(input())
  except:
      break
  if choice == 1:
      value = int(input())
      stack.push(value)
  elif choice == 2:
      stack.pop()
  elif choice == 3:
      stack.peek()
  elif choice == 4:
      if stack.is_empty():
          print("Stack is empty")
      else:
          print("Stack is not empty")
  elif choice == 5:
      print("Exiting...")
      break
  else:
      print("Invalid choice!")
