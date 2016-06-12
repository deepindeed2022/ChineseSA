__author__ = 'huang'


import os
import sys
from gensim import utils

class tCorpus:
    """Handle the corpus to common format"""
    SEGSIZE = 10000
    def __init__(self, fname):
        self.fname = fname
        self.logger = tCorpus.startlog()

    def get_texts(self, ofname):
        pass

    '''start log 
    '''
    @staticmethod
    def startlog(_format='%(asctime)s: %(levelname)s: %(message)s',_level=logging.INFO):
        import logging
        program = os.path.basename(__name__)
        logger = logging.getLogger(program)
        logging.basicConfig(format = _format)
        logging.root.setLevel(level=_level)
        return logger

class tWikiCorpus(tCorpus):
    def __init__(self, fname, lemmatize=False, dictionary={}, filter_namespaces=('0',)):
        super(fname)
        self.corpus = gensim.corpora.WikiCorpus(fname, lemmatize=lemmatize, dictionary=dictionary)
    def get_texts(self, ofname, space = ' '):
        i = 0
        with open(ofname, 'w') as output:
            for text in self.corpus.get_texts():
                output.write(space.join(text) + '\n')
                i = i + 1
                if i % tCorpus.SEGSIZE == 0:
                    self.logger.info('Saved ' + str(i) + ' articles')
        self.logger.info('Finished ' + str(i) + ' articles')
class tTextCorpus(tCorpus):
    pass

import logging  

if __name__=='__main__':
    if len(sys.argv) < 3:
        print(globals()['__doc__'] %locals())
        sys.exit(1)

    inp, outp = sys.argv[1:3]
    
    wiki = tWikiCorpus(inp, lemmatize=False, dictionary={})
    wiki.get_texts(outp, space = ' ')
   