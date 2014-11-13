rapgenii
========

src/
  contains code
src/aggregate.py
  aggregates every vote into a dictionary object.
  if run as a script, it tests the data in aggregationSampleData.py
src/qualityControl.py
  Determines the rap lines with the best rating using a wilson's score with
  85% certainty. Note that Wilson's score has many benefits over simpler
  scoring methods such as ratio or difference of upvotes and downvotes.
data/aggregationSampleData.py
  sample input and output data for aggregation
data/qualityControlSampleData.py
  sample input and output data for quality control
