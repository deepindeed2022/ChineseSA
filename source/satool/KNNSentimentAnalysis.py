#-*-encoding:utf8 -*-
from gensim.models import Word2Vec
from utility.function import startlog

class SentimentModel(object):
	"""docstring for SentimentModel"""
	def __init__(self, fmodel):
		self.wordmodel = Word2Vec.load(fmodel)
		self.logger = startlog()
		self._K = 10
		self.logger.info('Init SentimentModel')

	@property
	def K(self):
		return self._K

	def analysis(self, line):
		'''
		Using k-nearest-neighbor method to analysis the input message is negative or not
		'''
		self.logger.info('SentimentModel Analysis: %s' % line)
		l = []
		totwords = list()
		for word in line.split():
			l = self.wordmodel.most_similar(positive = word, topn= self.K)
			totwords.append(sorted(l, cmp = lambda x,y: x > y, 
									  key = lambda word: word[1]))
		return totwords
