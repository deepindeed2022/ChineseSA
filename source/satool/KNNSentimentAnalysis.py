#-*-encoding:utf8 -*-
from gensim.models import Word2Vec

from utility.function import startlog, getSemiWords, NTUSDDIR

class SentimentModel(object):
    """docstring for SentimentModel"""
    def __init__(self, fmodel, semitivedir = '../../data/ntusd/'):
        self.wordmodel = Word2Vec.load(fmodel)
        self.logger = startlog()
        self._K = 10
        self.semidict = getSemiWords(NTUSDDIR)
        self.logger.info('Init SentimentModel')

    @property
    def K(self):
        return self._K

    def knn_similar(self, line):
        '''
        Using k-nearest-neighbor method to analysis the input message is negative or not
        '''
        self.logger.info('SentimentModel Analysis: %s' % line)
        #line = seperate_word(line)
        l = []
        totwords = list()
        for word in line.split():
            try:
                l = self.wordmodel.most_similar(positive = word, topn= self.K)
                totwords.append(sorted(l, cmp = lambda x,y: x > y, 
                                          key = lambda word: word[1]))
            except KeyError, e:
                print word,' not found'
            
        return totwords
    def analysis_sentence(self, line):
        score = self.cal_sentence_score(line)
        if score > 0:
            self.logger.info(line+' Marked POSITIVE')
        else:
            self.logger.info(line+' Marked NEGATIVE')

    def sentence_ispositive(self, line):
        '''
        Get a vector to reprensent a doc
        Find the closed vec in model
        voted to decide the semition of the document
        '''
        pass

    def cal_sentence_score(self, line):

        def calweight(cosv, threshold = 0.5):
            if cosv > threshold:
                # Error: When a non-semitive word in sentence, there may exists many very
                # close word in the model, the weight will be very large.
                # So, the weight function should be redesigned for this case.
                return 1/(cosv*(1 - cosv))
            else:
                return 0

        def findsemitive(word, semidict):
            for (key, values) in semidict.iteritems():
                values = [i.decode('utf8') for i in values]
                if key == 'POSITIVE' and word in values:
                    return 1
                elif key == 'NEGATIVE' and word in values:
                    return -1
            return 0

        def isPositive(words, semitives):
            totle = [findsemitive(word, semitives) for word in words]
            posi_num = sum(filter(lambda x: x == 1, totle))
            nega_num = sum(filter(lambda x: x == -1, totle))
            maxnum = max([posi_num, abs(nega_num), len(words)- posi_num + nega_num])
            if maxnum == posi_num:
                return posi_num
            elif maxnum == abs(nega_num):
                return nega_num
            else:
                return 0

        # get the sentences's all word's similar word cos values
        totwords = self.knn_similar(line)

        # Decide the word's semitive
        sentenceScore = 0
        wordscores = []
        semitives = []
        for totword in totwords:
            cosvs = [i[1] for i in totword]
            words = [i[0] for i in totword]
            mean = sum(cosvs)/len(cosvs)
            
            wordScore = 0
            for i in range(len(words)):
                wordScore += findsemitive(words[i], self.semidict)*calweight(cosvs[i], mean)
            #wordScore = isPositive(totword, self.semidict)*calweight(max(cosvs), mean)
            wordscores.append(wordScore)
            semitives.append(wordScore > 0)
  
        # calculate the score
        i = 0
        while i < len(wordscores) - 1:
            if semitives[i] and semitives[i] == semitives[i+1]:
                wordscores[i] += wordscores[i+1]
                del wordscores[i + 1]
                del semitives[i + 1]
            elif not semitives[i] and semitives[i] == semitives[i+1]:
                wordscores[i] = - (wordscores[i] + wordscores[i+1])
                semitives[i] = True
                del wordscores[i + 1]
                del semitives[i + 1]
            else:
                i += 1
        sentenceScore = sum(wordscores)
        return sentenceScore