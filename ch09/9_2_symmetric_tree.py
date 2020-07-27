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

def symmetric_tree(root):
    def is_symmetric(t1,t2):
        # if both trees are empty they are symmetric
        if not t1 and not t2:
            return True
        elif t1 and t2: # both trees are not null
            return (t1.data == t2.data and is_symmetric(t1.left,t2.right) and is_symmetric(t1.right,t2.left))
        else:
            return False

    return not root or is_symmetric(root.left,root.right)

if __name__ == "__main__":
    bt = binaryTree()
    n3 = binaryTree(3,binaryTree(2),binaryTree(4))
    n8 = binaryTree(8,binaryTree(6),binaryTree(9))
    tree = binaryTree(5,n3,n8)
    
    symtree = binaryTree(5,binaryTree(3,None,binaryTree(6)),binaryTree(3,binaryTree(6),None))
    print(symmetric_tree(symtree))