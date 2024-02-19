# Create Node Class which accepts value,left,right
class Node:
    # constructor for teh class to initialize the class variables
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # ToString method to print the tree if required.
    def __str__(self):
        return "Node(" + str(self.value) + ")"


def inorder_walk(tree):
    if tree is not None:
        inorder_walk(tree.left)
        print(tree.value, end="")
        inorder_walk(tree.right)


def preorder_walk(tree):
    if tree is not None:
        print(tree.value, end="")
        preorder_walk(tree.left)
        preorder_walk(tree.right)


def postorder_walk(tree):
    if tree is not None:
        postorder_walk(tree.left)
        postorder_walk(tree.right)
        print(tree.value, end="")


# Create Tree by adding the Node inside node
tree = Node('A', Node('B', Node('D'), Node('E')), Node('C', Node('F'), Node('G')))

print('InOrder :', end="")
inorder_walk(tree)

print()
print('Pre Order :', end="")
preorder_walk(tree)

print()
print('Post Order :', end="")
postorder_walk(tree)
