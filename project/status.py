from enum import IntEnum


class Status(IntEnum):
    """
    Enumeration representing the possible statuses of a person.

    Attributes:
        EMPTY (int): Represents an empty node.
        HEALTHY (int): Represents a healthy person.
        INFECTED (int): Represents an infected person.
        CONTAGIOUS (int): Represents a contagious person.
        DEAD (int): Represents a deceased person.
        IMMUNE (int): Represents an immune person.
    """
    EMPTY = 0
    HEALTHY = 1
    INFECTED = 2
    CONTAGIOUS = 3
    DEAD = 4
    IMMUNE = 5
