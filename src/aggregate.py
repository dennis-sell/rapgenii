
from aggregationSampleData import *

def aggregate(vote, line, current_votes):
  upvotes, downvotes = current_votes.get(line, (0,0))
  if vote == Vote.U:
    current_votes[line] = (upvotes + 1, downvotes)
  elif vote == Vote.D:
    current_votes[line] = (upvotes, downvotes + 1)


def test_aggregate():
  votes = {}
  for vote, line in sample_votes_1:
    aggregate(vote, line, votes)
  print "aggregation passes test 1:", votes == output_1

  votes = {}
  for vote, line in sample_votes_2:
    aggregate(vote, line, votes)
  print "aggregation passes test 2:", votes == output_2


if __name__ == "__main__":
  test_aggregate()
