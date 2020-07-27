from binaryTree import binaryTree

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=",")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=",")

def preorder(root):
    if root:
        print(root.data,end=",")
        preorder(root.left)
        preorder(root.right)

if __name__ == "__main__":
    bt = binaryTree()
    n3 = binaryTree(3,binaryTree(2),binaryTree(4))
    n8 = binaryTree(8,binaryTree(6),binaryTree(9))
    tree = binaryTree(5,n3,n8)
    inorder(tree)
    print()
    preorder(tree)
    print()
    postorder(tree)