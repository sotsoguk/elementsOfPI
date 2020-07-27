from binaryTree import binaryTree
from collections import namedtuple
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

def height_balanced(root):
    balanceHeight = namedtuple('balanceHeight',('balanced','height'))

    def check_balance(tree):
        if not tree:
            return balanceHeight(True,-1)
        
        check_left = check_balance(tree.left)
        if not check_left.balanced:
            return balanceHeight(False,0)
        check_right = check_balance(tree.right)
        if not check_right.balanced:
            return balanceHeight(False,0)

        balanced = abs(check_left.height-check_right.height) <= 1
        height = max(check_left.height, check_right.height)+1
        return balanceHeight(balanced, height)
    return check_balance(root)

if __name__ == "__main__":
    bt = binaryTree()
    n3 = binaryTree(3,binaryTree(2),binaryTree(4))
    n8 = binaryTree(8,binaryTree(6),binaryTree(9))
    tree = binaryTree(5,n3,n8)
    print(height_balanced(tree))