class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None
  
def insert(root,key):
  if root is None:
    return Node(key)
  if key<root.data:
    root.left = insert(root.left,key)
  else:
    root.right = insert(root.right,key)
  
  return root

def postorder(root,result):
  if root:
    postorder(root.left, result)
    postorder(root.right, result)
    result.append(root.data)

n = int(input().strip())
arr = list(map(int, input().split()))

root = None
for val in arr:
  root = insert(root,val)

result =[]
postorder(root,result)
print(' '.join(map(str, result)))