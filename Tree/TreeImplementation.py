class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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

arr = [5, 3, 8, 1, 4, 7, 9]
root = None
for value in arr:
    root = append(root, value)

display_in_order(root)
