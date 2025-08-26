class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def append(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.data:
        root.left = append(root.left, value)
    else:
        root.right = append(root.right, value)
    return root

def countnodes(root):
    if root is None:
        return 0
    lc = countnodes(root.left)
    rc = countnodes(root.right)
    return 1 + lc + rc

n = int(input())
arr = list(map(int, input().split()))

root = None
for v in arr:
    root = append(root, v)

print(countnodes(root))
