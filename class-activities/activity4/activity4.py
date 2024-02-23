''' Example of a LinkedList implementation.'''


class Link():
    ''' This class represents a link between data items only.'''

    def __init__(self, data, next_link=None):
        self.data = data
        self.next = next_link

    def print_data(self):
        ''' Print the data contained in this link.'''
        print(self.data)

    def __str__(self):
        return str(self.data) + " --> " + str(self.next)


class LinkedList():
    ''' This class implements the operations of a simple linked list.'''

    def __init__(self):
        self.first = None

    def insert_first(self, data):
        '''Insert data at begining of a linked list.'''
        new_link = Link(data)
        new_link.next = self.first
        self.first = new_link

    def insert_last(self, data):
        '''Insert the data at the end of a linked list.'''
        new_link = Link(data)
        current = self.first

        if current is None:
            self.first = new_link
            return
        # Find the last and insert it there.
        while current.next is not None:
            current = current.next

        current.next = new_link

    def find_link(self, data):
        '''Find to which data is the link of a given data inside this linked list.'''
        current = self.first
        if current is None:
            return None

    # Search and find the position of the given data, the get the link if.
        while current.data != data:
            if current.next is None:
                return None

        current = current.next

        return current

    def delete_link(self, data):
        '''Removes the data from the list if exist and fix the link problems.'''

        current = self.first
        previous = self.first

        if current is None:
            return None

        while current.data != data:
            if current.next is None:
                return None

        previous = current

        current = current.next

        if current == self.first:
            self.first = self.first.next
        else:
            previous.next = current.next

        return current

    def __str__(self):
        return str(self.first)


class Stack():
    def __init__(self):
        self.list = LinkedList()

    def push(self, item):
        self.list.insert_first(item)

    def pop(self):
        val = self.list.first
        self.list.first = self.list.first.next
        return val

    def peek(self):
        return self.list.first


# Push is O(1), Pop is O(1), and peek is O(1)
