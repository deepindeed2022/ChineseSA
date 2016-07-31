# -*- coding: utf-8 -*-
import sys
import os.path
sys.path.append('../source/')
from  utility.function import tran2simple,seperate_word, remove_word, getSemiWords

import unittest
__doc__= """
Function Module Test Case:
module path in source.utility.function
author: Clython
"""
class functionTest(unittest.TestCase):
	def setUp(self):
		self.corpus = 'transchinese.txt'
		if os.path.exists(self.corpus+'.simple'):
			os.remove(self.corpus+'.simple')

	def testtrans2simple(self):
		line = ['開放中文轉換，是一個致力於中文簡繁轉換的項目，提供高質量詞庫和函數庫','的項目，提供高質量詞庫和函數']
		ret = tran2simple(line)
		exposeret = ['\xe5\xbc\x80\xe6\x94\xbe\xe4\xb8\xad\xe6\x96\x87\xe8\xbd\xac\xe6\x8d\xa2\xef\xbc\x8c\xe6\x98\xaf\xe4\xb8\x80\xe4\xb8\xaa\xe8\x87\xb4\xe5\x8a\x9b\xe4\xba\x8e\xe4\xb8\xad\xe6\x96\x87\xe7\xae\x80\xe7\xb9\x81\xe8\xbd\xac\xe6\x8d\xa2\xe7\x9a\x84\xe9\xa1\xb9\xe7\x9b\xae\xef\xbc\x8c\xe6\x8f\x90\xe4\xbe\x9b\xe9\xab\x98\xe8\xb4\xa8\xe9\x87\x8f\xe8\xaf\x8d\xe5\xba\x93\xe5\x92\x8c\xe5\x87\xbd\xe6\x95\xb0\xe5\xba\x93', '\xe7\x9a\x84\xe9\xa1\xb9\xe7\x9b\xae\xef\xbc\x8c\xe6\x8f\x90\xe4\xbe\x9b\xe9\xab\x98\xe8\xb4\xa8\xe9\x87\x8f\xe8\xaf\x8d\xe5\xba\x93\xe5\x92\x8c\xe5\x87\xbd\xe6\x95\xb0']
		assert(ret == exposeret)
			
	def testtrans2simplefile(self):
		import filecmp
		with open(self.corpus, 'r') as icorpus, \
			open(self.corpus+'.simple', 'w') as ocorpus:
			for line in icorpus.readlines():
				ocorpus.write(tran2simple(line) + '\n')
		assert(filecmp.cmp('transchinese.txt.simpletarget', self.corpus+'.simple'))

	def testseparateword(self):
		space = ' '
		line = '牛顿和莱布尼兹是微积分的发明者'
		ret = seperate_word(line, space)
		self.assertEqual(len(ret), 21)
		space = '*'
		ret = seperate_word(line, space)
		self.assertEqual(len(ret), 21)	

	def testremoveword(self):
		line = 'nihaod123456789wertyuiosdfghjklzbnm;是一致  力中文簡 的目，提供高量和函'.decode('utf8')
		expect = '是一致  力中文簡 的目提供高量和函'
		self.assertEqual(expect, remove_word(line))
		line = line.encode('utf8')
		self.assertNotEqual(expect, remove_word(line))

	def testgetSemiWords(self):
		self.assertNotEqual(None, getSemiWords())
		with self.assertRaises(IOError):
			getSemiWords(datadir=os.path.abspath('../datanotexit/ntusd/'))
		
		self.assertEqual({'noexist':None}, getSemiWords(fnames={'noexist':'noexist'}))

if __name__ == '__main__':
	print __doc__
	unittest.main()
