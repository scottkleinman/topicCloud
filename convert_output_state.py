# Configuration -- Use forward slashes, and make sure that output_state.gz has been unzipped
input_file_path = "Path to folder containing output_state file"
output_file_path = "Path to output folder/word-topic-counts.txt"

import itertools, os, re
tuples = []
# Read the output_state file
with open(input_file_path) as f:
    # Skip the first three lines
    for _ in xrange(3):
        next(f)
    #Create a list of type:topic combinations
    for line in f:
        line = re.sub('\s+', ' ', line) # Make sure the number of columns is correct
        try:		
            doc, source, pos, typeindex, type, topic = line.rstrip().split(' ')
            tuple = type+':'+topic
            tuples.append(tuple)
        except:
            print("Your source data cannot be parsed into a regular number of columns. 
            Please ensure that there are no spaces in your file names or file paths. It 
            may be easiest to open the outpt_state file in a spreadsheet using a space as 
            the delimiter and text as the field type. Data should only be present in columns 
            A to F. Please fix any misaligned data and run this script again.")
#print(tuples)

# Count the number of times each type-topic combo appears
from collections import defaultdict
topicCount = defaultdict(int)
for x in tuples:
  topicCount[x] += 1
#print(topicCount)

# Populate a topicCounts dict with type: topic:count
words = []
topicCounts = {}
for k, v in topicCount.iteritems():
    type, topic = k.split(':')
    count = int(v)
    tc = topic + ":" + str(count)
    if type in words:
        topicCounts[type] = topicCounts[type] + " " + tc
    else:
        topicCounts[type] = tc
    words.append(type)
#print(topicCounts)

# Add a word ID and print each word on a line with its topic:count list
out = ""
i = 0
for k, v in topicCounts.iteritems():
    out += str(i) + " " + k + " " + v + "\n"
    i += 1
#print(out)

# Write the output file
f = open(output_file_path,'w')
f.write(out) # Python will convert \n to os.linesep
f.close()

print('Done!')