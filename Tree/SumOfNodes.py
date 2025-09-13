class TreeNode:
    def __init__(self,data):
        self.data =  data
        self.right = None
        self.left = None

def append(root, data):
    if root is None:
        return TreeNode(data)
    if data < root.data:
        root.left = append(root.left, data)
    else:
        root.right = append(root.right, data)
    return root

def display_in_order(root):
    if root is not None:
        display_in_order(root.left)
        print(root.data, end=' ')
        display_in_order(root.right)

def sum_of_nodes(root):
    if root is None:
        return 0
    return root.data + sum_of_nodes(root.left) + sum_of_nodes(root.right)

root = None
arr = list(map(int, input().split()))

for value in arr:
    root = append(root, value)

print(sum_of_nodes(root))
display_in_order(root)