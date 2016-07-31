#! /usr/bin/python
#-*- encoding:utf8 -*-
import os
import sys
import logging
import os.path
import multiprocessing

from  gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

from utility.function import tran2simple, remove_word, seperate_word, startlog


class tCorpus(object):
    """Handle the corpus to common format"""
    SEGSIZE = 1000
    def __init__(self, fname, _lemmatize=False, _dictionary={}, filter_namespaces=('0',)):
        self.fname = fname
        self.logger = startlog()
        self.corpus = WikiCorpus(fname, lemmatize=_lemmatize, dictionary=_dictionary)
        self.traincorpusfname = None

    def getTexts(self, ofname, space = ' '):
        raise NotImplementedError('The getTexts method')

    def pretrain_model(self, space = ' '):
        raise NotImplementedError('__pretrain_model')

    def train_model(self, ofmodel, space = ' '):
        if self.traincorpusfname == None or not os.path.exists(self.traincorpusfname):
            ifname = self.pretrain_model(space)
        else:
            ifname = self.traincorpusfname
        self.logger.info('+++++++++++++++Train Model Start+++++++++++++++++\n')
        #
        # Calling Gensim 3rdparty lib, Training the word2vec word
        # more: http://radimrehurek.com/gensim/models/word2vec.html
        model = Word2Vec(LineSentence(ifname), size = 400, window = 5,
                    min_count = 2, workers = multiprocessing.cpu_count(),negative = 5)
        self.logger.info('+++++++++++++++Train Model Finished+++++++++++++++++\n')
        model.save(ofmodel)
        return (model, ofmodel)
class tTextCorpus(tCorpus):

    def pretrain_model(self, space = ' '):
        self.traincorpusfname = self.fname + '.traincorpus'
        # iter counter for articles
        i = 0
        with open(self.fname, 'r') as icorpus, \
            open(self.traincorpusfname, 'w') as ocorpus:
            for line in icorpus.readlines():
                # Convert the translated chinese to simple
                text = tran2simple(line)
                # seperate word using jieba
                text = seperate_word(text)
               
                # remove non-chinese word from corpus
                text = remove_word(line = text, encoding = 'utf8')
                # print text
                if text: ocorpus.write(text + '\n') 
                    
                i = i + 1
                if i % tCorpus.SEGSIZE == 0:
                    self.logger.info('PreVecModel: ' + str(i) + ' articles')
        self.logger.info('PreVecModel:' + str(i) + ' articles')

        return self.traincorpusfname

class tWikiCorpus(tCorpus):

    def __init__(self, fname, _lemmatize=False, _dictionary={}, filter_namespaces=('0',)):
        super(tWikiCorpus, self).__init__(fname, _lemmatize=False, _dictionary={}, filter_namespaces=('0',))  
        #TODO: using debug else  None
        self.textfile = None
        self.traincorpusfname = None

    # TODO:
    # Check the corpus's encode is GBK or UTF-8 or others encode method
    # Default Encode UTF-8
    def getTexts(self, ofname, space = ' '):
        if not os.path.isdir('../model'):
            os.mkdir('../model/')
        i = 0
        with open(ofname , 'w') as txtout:
            #with open(ofname, 'w') as output:
            for text in self.corpus.get_texts():
                # seperate chinese word
                text = space.join(text)
                # only debug use it
                txtout.write(text + '\n')

                i = i + 1
                if i % tCorpus.SEGSIZE == 0:
                    self.logger.info('Wiki to Text: ' + str(i) + ' articles')
        self.logger.info('Finished Wiki to Text:' + str(i) + ' articles')
        self.textfile = ofname
        return ofname

    def pretrain_model(self, space = ' '):
        # Assert the textfile is exist?
        if self.textfile == None:
            self.textfile = self.getTexts(self.fname + '.txt', space=' ')

        self.traincorpusfname = self.fname + '.traincorpus'
        # iter counter for articles
        i = 0
        with open(self.textfile, 'r') as icorpus, \
            open(self.traincorpusfname, 'w') as ocorpus:
            for line in icorpus.readlines():
                # Convert the translated chinese to simple
                text = tran2simple(line)
                # seperate word using jieba
                text = seperate_word(text)
               
                # remove non-chinese word from corpus
                text = remove_word(line = text, encoding = 'utf8')
                # print text
                if text: ocorpus.write(text + '\n') 
                    
                i = i + 1
                if i % tCorpus.SEGSIZE == 0:
                    self.logger.info('PreVecModel: ' + str(i) + ' articles')
        self.logger.info('PreVecModel:' + str(i) + ' articles')
        return self.traincorpusfname
