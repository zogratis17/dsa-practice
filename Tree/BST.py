class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert_into_bst(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

def count_nodes(root):
    if root is None:
        return 0
    leftcount = count_nodes(root.left)
    rightcount = count_nodes(root.right)
    return 1 + leftcount + rightcount
    
def sum_nodes(root, sumn):
    if root is None:
        return 0
    leftsum = sum_nodes(root.left, sumn)
    rightsum = sum_nodes(root.right, sumn)
    return root.val +leftsum + rightsum

def sum_leafnodes(root):
    if root is None:
      return 0
    if root.left is None and root.right is None:
        return root.val
    return sum_leafnodes(root.left) + sum_leafnodes(root.right)
    
def count_leafnodes(root):
    if root is None:
      return 0
    if root.left is None and root.right is None:
        return 1
    return count_leafnodes(root.left) + count_leafnodes(root.right)
    

n = int(input().strip())
values = list(map(int, input().split()))

root = None
for val in values:
    root = insert_into_bst(root, val)

total_nodes = count_nodes(root)
print(total_nodes)

print(f"sum of nodes = {sum_nodes(root, 0)}")

print(f"sum of leaf nodes = {sum_leafnodes(root)}")

external_nodes = count_leafnodes(root)
print(f"count of leaf nodes = {external_nodes}")

internal_nodes = total_nodes - external_nodes
print(f"count of internal nodes = {internal_nodes}")
