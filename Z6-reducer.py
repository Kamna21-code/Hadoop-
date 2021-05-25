#!/usr/bin/env python3
import sys
    
# Student ID: <Replace with your ID number>

# This reducer just sums up the counts of each key and will
# require significant changes to meet the assignment requirements.
       
counts = {}
# current_key = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py, splitting on tabs
    (type,sentiment,word,sum) = line.split('\t')
    count = int(sum)

    if not counts.get(type):
        counts[type] = {}

    if not counts[type].get(sentiment):
        counts[type][sentiment] = {}

    try:
        count = int(count)
        counts[type][sentiment][word] = counts[type][sentiment].get(word, 0) + count
    except ValueError:
        pass


for type, value1 in counts.items():
    for sentiment, value2 in value1.items():
        top_words_list = sorted(value2.items(), key=lambda kv: kv[1], reverse=True)[:5]
        print('%s\t%s\t%s' % (type, sentiment, " ".join([k for k,v in top_words_list])))
