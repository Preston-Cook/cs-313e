class Node():
    '''This class represents a single Node.'''

    def __init__(self, key):
        self.key = key
        self.lChild = None
        self.rChild = None

    def print_node(self, level=0):
        if self.rChild != None:
            self.rChild.print_node(level + 1)

        print(' ' * 4 * level + '->', self.key)

        if self.lChild != None:
            self.lChild.print_node(level + 1)

      # In-order traversal - left, center, right
    def inOrder(self, aNode):
        if (aNode != None):
            aNode.inOrder(aNode.lChild)
            print(aNode.key, end=" ")
            aNode.inOrder(aNode.rChild)

    # Pre-order traversal - center, left, right
    def preOrder(self, aNode):
        if (aNode != None):
            print(aNode.key, end=" ")
            aNode.preOrder(aNode.lChild)
            aNode.preOrder(aNode.rChild)

    # Post-order traversal - left, right, center
    def postOrder(self, aNode):
        if (aNode != None):
            aNode.postOrder(aNode.lChild)
            aNode.postOrder(aNode.rChild)
            print(aNode.key, end=" ")

    def bst_size(self, node: 'Node'):
        if not node:
            return 0
        return 1 + node.bst_size(node.rChild) + node.bst_size(node.lChild)


class BST():
    '''This class represents a Binary Search Tree.'''

    def __init__(self):
        self.root = None

    def print(self, level):
        self.root.print_node(level)

    # Search for a node with the key
    def search(self, key):
        current = self.root
        while ((current != None) and (current.key != key)):
            if (key < current.key):
                current = current.lChild
            else:
                current = current.rChild
        return current

    # Insert a node in the tree
    def insert(self, val):
        newNode = Node(val)

        if (self.root == None):
            self.root = newNode
        else:
            current = self.root
            parent = self.root
            # search
            while (current != None):
                parent = current
                if (val < current.key):
                    current = current.lChild
                else:
                    current = current.rChild
            # insert
            if (val < parent.key):
                parent.lChild = newNode
            else:
                parent.rChild = newNode

    # Find the node with the smallest value
    def minimum(self):
        current = self.root
        parent = current
        while (current != None):
            parent = current
            current = current.lChild
        return parent

    # Find the node with the largest value
    def maximum(self):
        current = self.root
        parent = current
        while (current != None):
            parent = current
            current = current.rChild
        return parent

    # Delete a node with a given key
    def delete(self, key):
        deleteNode = self.root
        parent = self.root
        isLeft = False

        # If empty tree
        if (deleteNode == None):
            return False

        # Find the delete node
        while ((deleteNode != None) and (deleteNode.key != key)):
            parent = deleteNode
            if (key < deleteNode.key):
                deleteNode = deleteNode.lChild
                isLeft = True
            else:
                deleteNode = deleteNode.rChild
                isLeft = False

        # If node not found
        if (deleteNode == None):
            return False

        # Delete node is a leaf node
        if ((deleteNode.lChild == None) and (deleteNode.rChild == None)):
            if (deleteNode == self.root):
                self.root = None
            elif (isLeft):
                parent.lChild = None
            else:
                parent.rChild = None

        # Delete node is a node with only left child
        elif (deleteNode.rChild == None):
            if (deleteNode == self.root):
                self.root = deleteNode.lChild
            elif (isLeft):
                parent.lChild = deleteNode.lChild
            else:
                parent.rChild = deleteNode.lChild

        # Delete node is a node with only right child
        elif (deleteNode.lChild == None):
            if (deleteNode == self.root):
                self.root = deleteNode.rChild
            elif (isLeft):
                parent.lChild = deleteNode.rChild
            else:
                parent.rChild = deleteNode.rChild

        # Delete node is a node with both left and right child
        else:
            # Find delete node's successor and successor's parent nodes
            successor = deleteNode.rChild
            successorParent = deleteNode

            while (successor.lChild != None):
                successorParent = successor

                successor = successor.lChild

            # Successor node right child of delete node
            if (deleteNode == self.root):
                self.root = successor
            elif (isLeft):
                parent.lChild = successor
            else:
                parent.rChild = successor

            # Connect delete node's left child to be successor's left child
            successor.lChild = deleteNode.lChild

            # Successor node left descendant of delete node
            if (successor != deleteNode.rChild):
                successorParent.lChild = successor.rChild

                successor.rChild = deleteNode.rChild

        return True

    def sort(self) -> list[int]:
        sorted_list = []
        return self.in_order_traversal(self.root, sorted_list)

    def in_order_traversal(self, node: Node, sorted_list: list[int]) -> list[int]:
        if node:
            self.in_order_traversal(node.lChild, sorted_list)
            sorted_list.append(node.key)
            self.in_order_traversal(node.rChild, sorted_list)

        return sorted_list

    def bst_median(self):
        sorted_elements = self.sort()
        lst_len = len(sorted_elements)

        mid = lst_len // 2

        if lst_len % 2 == 1:
            return sorted_elements[mid]

        return (sorted_elements[mid - 1] + sorted_elements[mid]) / 2

    def height(self):
        return self.node_height(self.root)

    def node_height(self, node: Node):
        if not node:
            return 0

        return 1 + max(self.node_height(node.lChild), self.node_height(node.rChild))

    def node_balanced(self, node: Node):
        if not node:
            return True

        l, r = self.node_height(node.lChild), self.node_height(node.rChild)

        if (abs(l - r) < 2) and self.node_balanced(node.lChild) and self.node_balanced(node.rChild):
            return True

        return False

    def is_balanced(self):
        return self.node_balanced(self.root)


###############################
#                             #
#   Example run of a BST run  #
#                             #
###############################


def main():
    bst = BST()

    bst.insert(10)
    bst.insert(40)
    bst.insert(5)
    bst.insert(15)
    bst.insert(22)
    bst.insert(4)

    bst.print(2)
    print("##############")
    bst.delete(10)
    bst.print(2)
    print("##############")

    print("Print In-Order")
    bst.root.inOrder(bst.root)

    print()
    print("Print Pre-Order")
    bst.root.preOrder(bst.root)

    print()
    print("Print Post-Order")
    bst.root.postOrder(bst.root)

    print('\n', bst.root.bst_size(bst.root))


if __name__ == '__main__':
    main()
