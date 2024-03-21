"""Assignment 7: Creates and evaluates an expression tree"""
#  File: ExpressionTree.py

#  Description:

#  Student Name: Crystal Hicks

#  Student UT EID: crh4624

#  Partner Name: Preston Cook

#  Partner UT EID: plc886

#  Course Name: CS 313E

#  Unique Number: 50775

#  Date Created: 3/20/24

#  Date Last Modified: 3/20/24

import sys

class Node():
    """Node of a BST with two children"""
    # constructor
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

    def print_node(self, level=0):
        """prints the node and its children"""
        if self.lchild is not None:
            self.lchild.print_node(level + 1)

        print(' ' * 3 * level + '->', self.data)

        if self.rchild is not None:
            self.rchild.print_node(level + 1)

    def get_height(self):
        """returns the height of the node"""
        if self.lchild is not None and self.rchild is not None:
            return 1 + max(self.lchild.get_height(), self.rchild.get_height())
        if self.lchild is not None:
            return 1 + self.lchild.get_height()
        if self.rchild is not None:
            return 1 + self.rchild.get_height()
        return 1

class Tree():
    """Binary Search Tree implementation with helper methods"""
    # constructor
    def __init__(self):
        self.root = None

    def print(self, level):
        """Prints a visualization of the BST"""
        self.root.print_node(level)

    def get_height(self):
        """returns height of the BST"""
        return self.root.get_height()

    def insert(self, data):
        """Inserts data into Binary Search Tree and creates a valid BST"""
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        parent = self.root
        curr = self.root
        # finds location to insert new node
        while curr is not None:
            parent = curr
            if data < curr.data:
                curr = curr.lchild
            else:
                curr = curr.rchild
        # inserts new node based on comparision to parent node
        if data < parent.data:
            parent.lchild = new_node
        else:
            parent.rchild = new_node
        return

    def get_minimum(self, node):
        """returns minimum node of the BST"""
        if node.lchild is None:
            return node
        return self.get_minimum(node.lchild)

    def get_maximum(self, node):
        """returns maximum node of the BST"""
        if node.rchild is None:
            return node
        return self.get_maximum(node.rchild)

    def range(self):
        """Returns the range of values stored in a binary search tree of integers."""
        if self.root is None:
            return []
        if self.get_height() == 1:
            return 0
        return self.get_maximum(self.root).data - self.get_minimum(self.root).data

    def get_level(self, level):
        """Returns a list of nodes at a given level from left to right"""
        level_nodes = []
        if self.root is None:
            return []
        queue = []
        queue.append(self.root)
        current_level = 0

        while current_level <= level:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop(0)
                if current_level == level:
                    level_nodes.append(node)
                if node.lchild is not None:
                    queue.append(node.lchild)
                if node.rchild is not None:
                    queue.append(node.rchild)
            current_level += 1

        return level_nodes

    def left_side_view(self):
        """returns the list of the node that you see from the left side"""
        left_side_nodes = []
        for level in range(self.get_height()):
            left_side_nodes.append(self.get_level(level)[0].data)
        return left_side_nodes

    def sum_leaf_nodes(self):
        """returns the sum of the value of all leaves"""
        leaf_sum = 0
        stack = [self.root]
        while len(stack) > 0:
            node = stack.pop()
            if node is None:
                continue
            if node.lchild is None and node.rchild is None:
                leaf_sum += node.data
            stack.append(node.lchild)
            stack.append(node.rchild)
        return leaf_sum

def make_tree(data):
    """Creates the BST from a list"""
    tree = Tree()
    for d in data:
        tree.insert(d)
    return tree

# Develop your own main function or test cases to be able to develop.
# Our tests on the Gradescop will import your classes and call the methods.
def main():
    """Tests for the BST helper methods"""
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line)) 	# converts elements into ints
    t1 = make_tree(tree1_input)
    t1.print(t1.get_height())

    print("Tree range is: ",   t1.range())
    print("Tree left side view is: ", t1.left_side_view())
    print("Sum of leaf nodes is: ", t1.sum_leaf_nodes())
    print("Height is: ", t1.get_height())
    print("Max is: ", t1.get_maximum(t1.root).data)
    print("Min is: ", t1.get_minimum(t1.root).data)
    print("##########################")

# Another Tree for test.
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line)) 	# converts elements into ints
    t2 = make_tree(tree2_input)
    t2.print(t2.get_height())

    print("Tree range is: ",   t2.range())
    print("Tree left side view is: ", t2.left_side_view())
    print("Sum of leaf nodes is: ", t2.sum_leaf_nodes())
    print("##########################")
# Another Tree
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line)) 	# converts elements into ints
    t3 = make_tree(tree3_input)
    t3.print(t3.get_height())

    print("Tree range is: ",   t3.range())
    print("Tree left side view is: ", t3.left_side_view())
    print("Sum of leaf nodes is: ", t3.sum_leaf_nodes())
    print("##########################")


if __name__ == "__main__":
    main()
