
sample_aggregated_votes_1 = {
    "Hello world": (1,2),
    "This isn't CIS 110": (1,0),
    "I'm having way too much fun with this": (2, 0),
}

output_1 = "Hello world"


sample_aggregated_votes_2 = {
    "i love rap, cause it da best": (3, 1),
    "I plan to become a productive member of society one day": (24, 10),
    "school is cool": (10, 10),
    "what is down homeslice": (1, 5),
}

# Note that even though the first option has a higher Upvote/Downvote ratio,
# the second one is chosen, because we are more certain about its ratio.
output_2 = "I plan to become a productive member of society one day"
