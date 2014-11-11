class Vote(Enum):
    U = 1
    D = 2


sample_votes_1 = [
    (D, "Hello world"),
    (D, "Hello world"),
    (U, "This isn't CIS 110"),
    (U, "I'm having way too much fun with this"),
    (U, "Hello world"),
]

output_1 = {
    "Hello world": (1,2),
    "This isn't CIS 110": (1,0),
    "I'm having way too much fun with this": (1, 0),
}

sample_votes_2 = [
    (U, "i love rap, cause it da best"),
    (D, "I plan to become a productive member of society one day"),
    (D, "school is cool"),
    (U, "school is cool"),
    (U, "school is cool"),
    (D, "school is cool"),
    (U, "i love rap, cause it da best"),
    (U, "what is down homeslice"),
    (U, "i love rap, cause it da best"),
    (D, "I plan to become a productive member of society one day"),
]

output_2 = {
    "i love rap, cause it da best": (3, 0),
    "I plan to become a productive member of society one day": (0, 2),
    "school is cool": (2, 2),
    "what is down homeslice": (1, 0),
}
