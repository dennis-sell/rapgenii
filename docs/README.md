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
docs/
  contains documentation, mainly from preplanning
docs/frontPageMockUp.jpg
  this is what people will see when they go to the site. It will show raps in
  progess and raps which are recently finished.
docs/rapInProgressMockUp.jpg
  This is what users will see when they go to a rap in progress. On the left
  will be displayed the rap in its current state, and on the right we will see
  suggestions for the next two lines, as well as the upvotes and downvotes.
