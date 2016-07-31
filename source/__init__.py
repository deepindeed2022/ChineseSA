__version__ = '0.1'
__author__ = 'Clython Cao'
__doc__ = 	"""
			Hello, Thanks for your attentions!
			My software is used for Chinese Semitation Analysis, I use the word2vec to represents
			chinese words, and you should run as following:
			First, you should ensure the python-scipy and python-numpy have been installed on your programming environment.
			Second, you should using pip install gensim for word2vec model training
			Finally, you can install jieba package for python separate chinese word or ignore this step.

			Copy right reserved (Clython Cao), create:2016-06-13
			"""
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

