class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printInorder(node):
    if node is None:
        return
    printInorder(node.left)
    print(node.data)
    printInorder(node.right)


def search(node, value):
    if node is None:
        return False
    if node.data == value:
        return True
    elif node.data > value:
        return search(node.left, value)
    else:
        return search(node.right, value)


def printPreOrder(node):
    if node is None:
        return
    print(node.data)
    printPreOrder(node.left)
    printPreOrder(node.right)


def printPostOrder(node):
    if node is None:
        return
    printPostOrder(node.left)
    printPostOrder(node.right)
    print(node.data)
