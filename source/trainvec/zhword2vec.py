import logging
import os.path
import sys
import multiprocessing


from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence


def zhword2vec(ifname, fmodel):
    '''Training the word2vec word
    more: http://radimrehurek.com/gensim/models/word2vec.html

    '''
    model = Word2Vec(LineSentence(ifname), size = 400, window = 5,
                    min_count = 2, workers = multiprocessing.cpu_count(),negative = 5)
    model.save(fmodel)
    # model.save_word2vec_format(fword2vec, binary=False)

