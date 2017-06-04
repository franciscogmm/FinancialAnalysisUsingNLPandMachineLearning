import csv
import pandas as pd
import nltk
from nltk import FreqDist,ngrams
from nltk.corpus import stopwords
import string
from os import listdir
from os.path import isfile, join

def ngram_list(file,n):
    f = open(file,'rU')
    raw = f.read()
    raw = raw.replace('\n',' ')
    #raw = raw.decode('utf8')
    #raw = raw.decode("utf-8", 'ignore')
    ngramz = ngrams(raw.split(),n)
    return ngramz
def IsNotNull(value):
	    return value is not None and len(value) > 0

mypath = '/Users/francis/Documents/FORDHAM/2nd Term/Text Analytics/' #path where files are located
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

dict_p = []
f = open('positive.txt', 'r')
for line in f:
	t = line.strip().lower()
	if IsNotNull(t):
		dict_p.append(t)
f.close

dict_n = []
f = open('negative.txt', 'r')
for line in f:
	t = line.strip().lower()
	if IsNotNull(t):
		dict_n.append(t)
f.close
totallist = []
rowlist = []
qa = 0
qb = 0
counti = 0
for i in onlyfiles:
    if i.endswith('.txt'):
        # get code
        j = i.replace('.txt','')
        # string filename
        file = mypath + str(i)
        print i

        f = open(file,'rU')
        raw = f.read()
        #print type(raw)
        raw = [w.translate(None, string.punctuation) for w in raw]
        raw = ''.join(raw)
    	raw = raw.replace('\n','')
    	raw = raw.replace(' ','')
    	#print raw
    	qa = 0
    	qb = 0
        for word in dict_p:
			if word in raw:
				qa += 1

    	for word in dict_n:
			if word in raw:
				qb += 1

    	qc = qa - qb

    	if qc > 0:
			sentiment = 'POSITIVE'
    	elif qc == 0:
			sentiment = 'NEUTRAL'
    	else:
			sentiment = 'NEGATIVE'

    	rowlist.append(i)
    	rowlist.append(qa)
    	rowlist.append(qb)
    	rowlist.append(qc)
    	rowlist.append(sentiment)

    	print counti
    	counti += 1
    	totallist.append(rowlist)

    	rowlist = []




    else:
        pass

labels = ('file', 'P', 'N', 'NET', 'SENTIMENT')
df = pd.DataFrame.from_records(totallist, columns = labels)

df.to_csv('oursentiment.csv', index = False)


#print dict_p


# allbigrams.append(ngram_list(file,2))
        # print i + ' BIGRAM - OK'
        # alltrigrams.append(ngram_list(file,3))
        # print i + ' TRIGRAM - OK'
        # allfourgrams.append(ngram_list(file,4))
        # print i + ' FOURGRAM - OK'
        # allfivegrams.append(ngram_list(file,5))
        # print i + ' TRIGRAM - OK'
        # allsixgrams.append(ngram_list(file,6))
        # print i + ' SIXGRAM - OK'
        # allsevengrams.append(ngram_list(file,7))
        # print i + ' SEVENGRAM - OK'
        # alleightgrams.append(ngram_list(file,8))
        # print i + ' EIGHTGRAM - OK'