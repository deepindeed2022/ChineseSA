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
	print('please sudo pip install gensim and jieba python-package')
finally:
	print("---------Check package finished!---------")

