import os
import os.path

NTUSDDIR = os.path.abspath('../../data/ntusd/')

def count(words, poslist, neglist, threshold = 0.25):
	'''Function counting the word in list:words which is postive or negative word
	@param: words
	@param: poslist the list of postive words
	@param: neglist the list of negative words
	@param: threshold , the value is recongenize the words is postive or not
	'''
	posValue = 0
	negValue = 0

	for (first, cosval) in words:
		if first in poslist:
			posValue += cosval
		elif first in neglist:
			negValue += cosval
	val = (posValue - negValue)

	if val > threshold: return 1 
	return -1 if val < -threshold else 0

	
# TODO:
# Load negative and postive word from file
def calweight(cosv, threshold = 0.5):
	if cosv > threshold:
		return 1/(cosv*(1 - cosv))
	else:
		return 0
# for i in range(1,1000):
# 	print calweight(float(i)/1000)
ret = [[(u'\u5965\u65af\u5361\u91d1\u50cf\u5956', 0.6809592843055725), (u'\u5965\u65af\u5361\u5956', 0.673301637172699), (u'\u91d1\u7403\u5956', 0.6209549307823181), (u'\u4e1c\u5c3c\u5956', 0.6041178107261658), (u'\u91d1\u68d5\u6988\u5956', 0.5911039113998413), (u'\u5c0f\u91d1\u4eba', 0.5633037686347961), (u'\u827e\u7f8e\u5956', 0.5571725964546204), (u'\u91d1\u718a\u5956', 0.5495156049728394), (u'\u6258\u5c3c\u5956', 0.5403841137886047), (u'\u738b\u5c14\u5fb7', 0.534138023853302)]]

def findsemitive(word, semidict):
	for (key, values) in semidict.iteritems():
		if key == 'POSTIVE' and word in values:
			return 1
		elif key == 'NEGATIVE' and word in values:
			return -1
	return 0

def cal_sentence_score(totwords, semidict):
	sentenceScore = 0
	for totword in totwords:
		cosvs = [i[1] for i in totword]
		words = [i[0] for i in totword]
		mean = sum(ll)/len(cosvs)
		for i in range(len(words)):
			sentenceScore += findsemi(words[i], semidict)*calweight(cosvs[i], mean)	
	return sentenceScore



def Score(wordscores, semitives):
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

wordscores = [1, 2, -3, -4]
semitives = [True, True, False, False]
print 'score: ',Score(wordscores, semitives)

wordscores = [0, 1, 0, 2, -3, -4]
semitives = [True, True, False, True, False, False]
print 'score: ',Score(wordscores, semitives)