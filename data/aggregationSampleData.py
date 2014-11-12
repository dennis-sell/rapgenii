from enum import Enum

class Vote(Enum):
    U = 1
    D = 2


sample_votes_1 = [
    (Vote.D, "Hello world"),
    (Vote.D, "Hello world"),
    (Vote.U, "This isn't CIS 110"),
    (Vote.U, "I'm having way too much fun with this"),
    (Vote.U, "Hello world"),
]

output_1 = {
    "Hello world": (1,2),
    "This isn't CIS 110": (1,0),
    "I'm having way too much fun with this": (1, 0),
}

sample_votes_2 = [
    (Vote.U, "i love rap, cause it da best"),
    (Vote.D, "I plan to become a productive member of society one day"),
    (Vote.D, "school is cool"),
    (Vote.U, "school is cool"),
    (Vote.U, "school is cool"),
    (Vote.D, "school is cool"),
    (Vote.U, "i love rap, cause it da best"),
    (Vote.U, "what is down homeslice"),
    (Vote.U, "i love rap, cause it da best"),
    (Vote.D, "I plan to become a productive member of society one day"),
]

output_2 = {
    "i love rap, cause it da best": (3, 0),
    "I plan to become a productive member of society one day": (0, 2),
    "school is cool": (2, 2),
    "what is down homeslice": (1, 0),
}
