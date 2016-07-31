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
from utility.function import seperate_word, remove_word
class SentimentModelTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.samodel = SentimentModel('../model/1/zhwiki.model')

    def test_knn_similar(self):
        similars = self.samodel.knn_similar('奥斯卡'.decode('utf8'))
        ret = [[(u'\u5965\u65af\u5361\u91d1\u50cf\u5956', 0.6809592843055725), (u'\u5965\u65af\u5361\u5956', 0.673301637172699), (u'\u91d1\u7403\u5956', 0.6209549307823181), (u'\u4e1c\u5c3c\u5956', 0.6041178107261658), (u'\u91d1\u68d5\u6988\u5956', 0.5911039113998413), (u'\u5c0f\u91d1\u4eba', 0.5633037686347961), (u'\u827e\u7f8e\u5956', 0.5571725964546204), (u'\u91d1\u718a\u5956', 0.5495156049728394), (u'\u6258\u5c3c\u5956', 0.5403841137886047), (u'\u738b\u5c14\u5fb7', 0.534138023853302)]]
        self.assertEqual(ret, similars)
        similars = self.samodel.knn_similar('使用  语料库'.decode('utf8'))
        self.assertEqual(len(similars), 2)
    def test_cal_sentence_score(self):
        def handlesentence(line):
            text = seperate_word(line)
            text = remove_word(line = text, encoding = 'utf8')
            return text.decode('utf8')
        
        point2 = '不值这个价格,不好'
        self.assertLess(self.samodel.cal_sentence_score(handlesentence(point2)), 0)
        point = '裙子很仙，和图片一模一样，价格也便宜，喜欢的朋友们不要犹豫了'
        self.assertGreater(self.samodel.cal_sentence_score(handlesentence(point)), 0)
    def test_analysis_sentence(self):
        pass
if __name__ == '__main__':

    unittest.main()
