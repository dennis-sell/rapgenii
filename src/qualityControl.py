from math import sqrt
from qualityControlSampleData import *

def wilson_score(upvotes, downvotes):
  n = upvotes + downvotes
  if n == 0:
    return 0

  z = 1.0 # Z-score of lower bound
  phat = float(upvotes) / n
  return (phat + z*z/(2*n) - z * sqrt((phat*(1-phat)+z*z/(4*n))/n))/(1+z*z/n)


def best_line(votes):
  if not votes:
    return None
  all_items = votes.items()
  wilson_scores = [(wilson_score(u, d), line) for line, (u, d) in all_items]
  wilson_scores.sort(reverse=True)
  # returns line with highest wilson score
  return wilson_scores[0][1]


if __name__=="__main__":
  print best_line(sample_aggregated_votes_1) == output_1
  print best_line(sample_aggregated_votes_2) == output_2
