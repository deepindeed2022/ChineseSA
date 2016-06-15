import os
import os.path

NTUSDDIR = os.path.abspath('../../data/ntusd/')

def count(words, poslist, neglist, threshold = 0.25):
	'''Function counting the word in list:words which is postive or negative word
	@param: words
	@param: poslist the list of postive words
	@param: neglist the list of negative words
	@param: threshold , the value is recongenize the words is postive or not
	'''
	posValue = 0
	negValue = 0

	for (first, cosval) in words:
		if first in poslist:
			posValue += cosval
		elif first in neglist:
			negValue += cosval
	val = (posValue - negValue)

	if val > threshold: return 1 
	return -1 if val < -threshold else 0

def load(fname):
	words = []
	with open(fname, 'r') as f:
		for line in f.readlines():
			words.append(line.strip())
	return words

for i in load(os.path.join(NTUSDDIR,'ntusd-negative.txt')):
	print i
	
# TODO:
# Load negative and postive word from file
