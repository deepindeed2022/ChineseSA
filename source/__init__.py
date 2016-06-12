__version__ = '0.01'
__author__ = 'Clython'

try:
	import scipy
except ImportError:
	print('Please install Scipy package')
	
try:
	import gensim
	import jieba
except ImportError:
	import sys
	sys.path.append('../3rdpart/')
finally:
	print("---------Check package finished!---------")
