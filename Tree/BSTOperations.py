class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def deleteNode(root, key):
    if root is None:
        return root
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None and root.right is None:
            root = None
            return root
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.val = temp.val
        root.right = deleteNode(root.right, temp.val)
    return root

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.val, end=" ")
        inOrder(root.right)

def main():
    root = None
    keys = [50, 30, 20, 40, 70, 60, 80]
    for key in keys:
        root = insert(root, key)
    print("Inorder traversal of the given tree")
    inOrder(root)
    print("\nDelete 20")
    root = deleteNode(root, 20)
    print("Inorder traversal after deletion")
    inOrder(root)
    print("\nDelete 30")
    root = deleteNode(root, 30)
    print("Inorder traversal after deletion")
    inOrder(root)
    print("\nDelete 50")
    root = deleteNode(root, 50)
    print("Inorder traversal after deletion")
    inOrder(root)

if __name__ == "__main__":
    main()