#-*-encoding:utf8 -*-
__doc__= """
SentimentModel Module Test Case:
module path in source.satool.KNNSentimentAnalysis
author: Clython
"""
import sys
sys.path.append('../source/')
import unittest
from  satool.KNNSentimentAnalysis import SentimentModel

class SentimentModelTest(unittest.TestCase):
	def setUp(self):
		self.samodel = SentimentModel('../model/zhwiki.model')

	def test_Analysis(self):
		similars = self.samodel.analysis('奥斯卡'.decode('utf8'))
		ret = [[(u'\u5965\u65af\u5361\u91d1\u50cf\u5956', 0.6809592843055725), (u'\u5965\u65af\u5361\u5956', 0.673301637172699), (u'\u91d1\u7403\u5956', 0.6209549307823181), (u'\u4e1c\u5c3c\u5956', 0.6041178107261658), (u'\u91d1\u68d5\u6988\u5956', 0.5911039113998413), (u'\u5c0f\u91d1\u4eba', 0.5633037686347961), (u'\u827e\u7f8e\u5956', 0.5571725964546204), (u'\u91d1\u718a\u5956', 0.5495156049728394), (u'\u6258\u5c3c\u5956', 0.5403841137886047), (u'\u738b\u5c14\u5fb7', 0.534138023853302)]]
		assert(ret == similars)
		similars = self.samodel.analysis('使用  语料库'.decode('utf8'))
		assert(len(similars) == 2)
	
if __name__ == '__main__':
	print __doc__
	unittest.main()
