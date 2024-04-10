"""Assignment 7: Creates and evaluates an expression tree"""
#  File: ExpressionTree.py

#  Description:

#  Student Name: Crystal Hicks

#  Student UT EID: crh4624

#  Partner Name: Preston Cook

#  Partner UT EID: plc886

#  Course Name: CS 313E

#  Unique Number: 50775

#  Date Created: 3/5/24

#  Date Last Modified: 3/14/24

import sys
import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '//': operator.floordiv,
    '%': operator.mod,
    '**': operator.pow
}

operators = ['+', '-', '*', '/', '//', '%', '**']


class Stack(object):
    """Standard stack implementation used to create expression tree"""

    def __init__(self):
        self.stack = []

    def push(self, data):
        """pushes data onto the top of the stack"""
        self.stack.append(data)

    def pop(self):
        """pops and returns the item from the top of the stack"""
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        """returns true if the stack has no elements"""
        return len(self.stack) == 0


class Node(object):
    """Each node of the tree has data that is a parenthese, operator, or operand
        and has a left and right child
    """

    def __init__(self, data=None, l_child=None, r_child=None):
        self.data = data
        self.l_child = l_child
        self.r_child = r_child


class Tree(object):
    """Expression tree, can evaluate valid infix expressions"""

    def __init__(self):
        self.root = None

    def create_tree(self, expr: str):
        """creates the expression tree from input expr"""
        stack = Stack()
        tokens = expr.split()
        self.root = Node()

        current_node = self.root
        for token in tokens:
            if token == "(":
                current_node.l_child = Node()
                stack.push(current_node)
                current_node = current_node.l_child
            elif token in operators:
                current_node.data = token
                stack.push(current_node)
                current_node.r_child = Node()
                current_node = current_node.r_child
            elif token == ")":
                current_node = stack.pop()
            else:
                current_node.data = token
                current_node = stack.pop()
    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated

    def evaluate(self, node: Node):
        """returns the value of the expression after being calculated"""
        if node is None:
            return 0

        if node.l_child is None and node.r_child is None:
            return node.data
        left_total = self.evaluate(node.l_child)
        right_total = self.evaluate(node.r_child)

        return ops[node.data](float(left_total), float(right_total))

    def pre_order(self, node: Node) -> str:
        """returns a string of the expression written in preorder notation"""
        if node is None:
            return ""
        return node.data + " " + self.pre_order(node.l_child) + self.pre_order(node.r_child)

    def post_order(self, node: Node) -> str:
        """returns a string of the expression written in postorder notation"""
        if node is None:
            return ""
        return self.post_order(node.l_child) + self.post_order(node.r_child) + " " + node.data

# you should NOT need to touch main, everything should be handled for you


def main():
    """main method"""
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()

    tree = Tree()
    tree.create_tree(expr)
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())


if __name__ == "__main__":
    main()
