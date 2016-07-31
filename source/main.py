#-*-encoding:utf8 -*-
__author__ = 'Clython Cao'
__doc__ =   """
            Hello, Thanks for your attentions!
            My software is used for Chinese Semitation Analysis, I use the word2vec to represents
            chinese words, and you should run as following:
            python main.py your_corpus_file_path your_model_exposed_path
            After running a long time, you will get a vecmodel for chinese words in your input path.

            Copy right reserved (Clython Cao), create:2016-06-13
            """
import sys
import os
import time
from trainvec.trainvecmodel import tWikiCorpus,tTextCorpus

class DataLossError(Exception):
    pass

def trainwordvec(ifname, ofname, rebuild = False):
    if os.path.isfile(ofname) and rebuild:
        ofname = ofname +'.' +str(time.time())

    if not os.path.isfile(ofname) or rebuild:
        wiki = tWikiCorpus(ifname, _lemmatize=False, _dictionary={})
        wiki.train_model(ofname)


if __name__=='__main__':
    if len(sys.argv) < 3:
        print(globals()['__doc__'] %locals())
        sys.exit(1)

    inp, outp =sys.argv[1:3]
    trainwordvec(inp, outp, False)