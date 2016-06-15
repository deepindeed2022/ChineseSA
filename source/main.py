import sys
import os
from trainvec.preanalysis import tWikiCorpus

import time

class DataLossError(Exception):
    pass

def trainwordvec(ifname, ofname, rebuild = False):
    if os.path.isfile(ofname):
        ofname = ofname +'.' +str(time.time())

    # tmpfile = os.path.abspath('../data/temp.dat')
    if not os.path.isfile(ofname) or rebuild:
        wiki = tWikiCorpus(ifname, _lemmatize=False, _dictionary={})
        wiki.train_model(ofname)
    # zhword2vec(tmpfile, ofname)

if __name__=='__main__':
    if len(sys.argv) < 3:
        print(globals()['__doc__'] %locals())
        sys.exit(1)

    inp, outp =sys.argv[1:3]
    trainwordvec(inp, outp, True)