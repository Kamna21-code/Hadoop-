#!/usr/bin/env python3
import sys
import string, nltk
from nltk.tokenize import word_tokenize

excluded = {"i", "not", "is", "and", "or", "the", "this", "a", "it", "of", "was", "to", "that", "in", "for", "movie", "film", "with", "as", "are", "had"}

def eprint(*args, **kwargs):
	print(args,file=sys.stderr,**kwargs)


def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


for line in sys.stdin:
	line = line.strip()
	(type,review,sentiment) = line.split('\t')
	review = review.strip()
	review = review.lower()
	text_tokens = word_tokenize(review)

	tokens_alphanumeric = [word for word in text_tokens if word.isalpha()]
	tokens_without_sw = [word for word in tokens_alphanumeric if not word in excluded]
	filtered_review = (" ").join(tokens_without_sw)

	words_dict = word_count(filtered_review)


	for k,v in words_dict.items():
		print('%s\t%s\t%s\t%s' % (type,sentiment,k,v))


