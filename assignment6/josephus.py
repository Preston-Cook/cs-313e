"""
    File: employee.py
    Description: Given a list of tuples representing intervals,
                The program returns a list of collapsed intervals
    Student Name: Crystal Hicks
    Student UT EID: crh4624
    Partner Name: Preston Cook
    Partner UT EID: plc886
    Course Name: CS 313E
    Unique Number: 50775
    Date Created: 28 February 2023
    Date Last Modified: 28 February 2023
    Input: num_soldiers is the number of links to be in the circular list.
           start_count is the link on which delete_after starts counting.
           elim_num is the interval counted around the circular list 
           before each time a link is deleted.
    Output: the order of links (soldiers) that are deleted.
"""

import sys

class Link():
    ''' This class represents a link between data items only.'''
    def __init__ (self, data, next_link = None):
        self.data = data
        self.next = next_link

    def print_data(self):
        ''' Print the data contained in this link.'''
        print(self.data)

    def __str__(self):
        return str(self.data) + " --> " + str(self.next.data)


class CircularList:
    '''This class represents a circular list where the last element is linked to the first'''
    # Constructor
    def __init__ ( self , num_links = 0):
        '''creates a circular list populated with elements num_links'''
        self.first = None
        for n in range(1, num_links+1):
            self.insert(n)

    def is_empty (self):
        '''returns true if the list is empty'''
        return self.first is None

    # Insert an element (value) in the list
    def insert (self, data):
        '''Insert the data at the end of a circular list.'''
        new_link = Link(data)
        current = self.first

        if current is None:
            self.first = new_link
            new_link.next = new_link
            return
        # Find the last and insert it there.
        while current.next is not self.first:
            current = current.next

        current.next = new_link
        new_link.next = self.first

    # Find the Link with the given data (value)
    # or return None if the data is not there
    def find (self, data):
        '''Find to which data is the link of a given data inside this linked list.'''
        current = self.first
        if current is None:
            return None

        # Search and find the position of the given data, the get the link if.
        while current.data != data:
            if current.next is self.first:
                return None

            current = current.next

        return current

    # Delete a Link with a given data (value) and return the Link
    # or return None if the data is not there
    def delete (self, data):
        '''Removes the data from the list if exist and fix the link problems.'''

        current = self.first
        previous = self.first

        if current is None:
            return None

        while current.data != data:
            if current.next is self.first:
                return None

            previous = current

            current = current.next

        if current == self.first:
            if current.next == self.first:
                self.first = None  # Handle deletion of the only node in the list

            else:
                while current.next != self.first:  # Find the last node
                    current = current.next
                current.next = self.first.next  # Update the last node's next pointer
                self.first = self.first.next  # Update the first node
        else:
            previous.next = current.next

        return current

    # Delete the nth Link starting from the Link start
    # Return the data of the deleted Link AND return the
    # next Link after the deleted Link in that order
    def delete_after ( self, start, n ):
        '''delete the nth Link starting from Link start'''
        current = self.find(start)
        if current is None:
            return None, None

        for _ in range(n-1):
            current = current.next
        deleted_link = current
        print(deleted_link.data)
        return self.delete(deleted_link.data), deleted_link.next

    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__ ( self ):
        if self.first is None:
            return "[]"

        elements = []
        current = self.first
        while True:
            elements.append(str(current.data))
            current = current.next
            if current == self.first:
                break

        return "[" + ", ".join(elements) + "]"

def main():
    '''reads from input file and calls delete_after until the circular list is empty'''
    # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int (line)

    # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int (line)

    # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int (line)

    soldiers = CircularList(num_soldiers)
    while not soldiers.is_empty():
        deleted_soldier, next_soldier = soldiers.delete_after (start_count, elim_num)
        str(deleted_soldier)
        start_count = next_soldier.data

if __name__ == "__main__":
    main()
