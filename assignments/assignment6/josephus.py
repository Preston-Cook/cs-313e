import sys


class Link:
    def __init__(self, val):
        self.val = val
        self.next: None | 'Link' = None


class CircularList(object):
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_link = Link(data)

        if self.head is None:
            self.head = new_link
            self.head.next = self.head
            return

        cur = self.head.next

        while cur.next != self.head:
            cur = cur.next

        new_link.next = self.head
        cur.next = new_link

    def find(self, data):
        if self.head is None:
            return None
        current = self.head
        while True:
            if current.val == data:
                return current
            current = current.next
            if current == self.head:
                return None

    def delete(self, data):
        if self.head is None:
            return None
        if self.head.val == data:
            if self.head.next != self.head:
                self.head = self.head.next
            else:
                self.head = None
            return data

        prev = self.head
        cur = self.head.next

        while cur != self.head:
            if cur.val == data:
                prev.next = cur.next
                return data
            prev = cur
            cur = cur.next

        return None

    def delete_after(self, start: Link, n: int):
        if start is None:
            return None, None
        current = start
        for _ in range(n - 1):
            current = current.next
        next_link = current.next
        current.next = current.next.next
        return next_link.val, current.next

    def __str__(self) -> str:
        if self.head is None:
            return "[]"
        result = "["
        current = self.head
        while True:
            result += str(current.val)
            current = current.next
            if current == self.head:
                break
            result += ", "
        result += "]"
        return result


def main():
    # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int(line)

    # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int(line)

    # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int(line)

    circle = CircularList()

    for i in range(1, num_soldiers + 1):
        circle.insert(i)

    start = circle.find(start_count)

    while circle.head:
        print(circle)
        start = circle.delete_after(start, elim_num)

    print(circle)


# your code
if __name__ == "__main__":
    main()
