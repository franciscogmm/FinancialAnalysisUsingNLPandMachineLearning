import csv
import pandas as pd
from time import time, sleep
import numpy as np
import nltk
import string
import ast
import re
import os
import sys
import multiprocessing 
from os import listdir
from os.path import isfile, join
csv.field_size_limit(sys.maxsize)
#os.system("taskset -p 0xff %d" % os.getpid())
def IsNotNull(value):
	    return value is not None and len(value) > 0

totallist = []

#create +/- word-dict
#Bing Liu's dictionary
dict_p = []
f = open('positive-words.txt', 'r')
for line in f:
	t = line.strip().lower()
	if IsNotNull(t):
		dict_p.append(t)
f.close

dict_n = []
f = open('negative-words.txt', 'r')
for line in f:
	t = line.strip().lower()
	if IsNotNull(t):
		dict_n.append(t)
f.close

#change to MASTER DICTIONARY
dict_n2 = []
f = open('negative - master dictionary.txt', 'r')
for line in f:
	t = line.strip().lower()
	if IsNotNull(t):
		dict_n2.append(t)
f.close

dict_p2 = []
f = open('positive - master dictionary.txt', 'r')
for line in f:
	t = line.strip().lower()
	if IsNotNull(t):
		dict_p2.append(t)
f.close

#EXTENDED SENTIMENT
dict_uncertainty = []
f = open('uncertainty - master dictionary.txt', 'r')
for line in f:
	t = line.strip().lower()
	if IsNotNull(t):
		dict_uncertainty.append(t)
f.close
dict_litigious = []
f = open('litigious - master dictionary.txt', 'r')
for line in f:
	t = line.strip().lower()
	if IsNotNull(t):
		dict_litigious.append(t)
f.close
dict_constraining = []
f = open('constraining - master dictionary.txt', 'r')
for line in f:
	t = line.strip().lower()
	if IsNotNull(t):
		dict_constraining.append(t)
f.close
dict_superfluous = []
f = open('superfluous - master dictionary.txt', 'r')
for line in f:
	t = line.strip().lower()
	if IsNotNull(t):
		dict_superfluous.append(t)
f.close
dict_interesting = []
f = open('interesting - master dictionary.txt', 'r')
for line in f:
	t = line.strip().lower()
	if IsNotNull(t):
		dict_interesting.append(t)
f.close
dict_modal = []
f = open('modal - master dictionary.txt', 'r')
for line in f:
	t = line.strip().lower()
	if IsNotNull(t):
		dict_modal.append(t)
f.close


rowlist = []
rowlist2 = []
newlist = []
netcnt2 = 0
netcnt = 0
counti = 1
qa = 0
qb = 0
qa2 = 0
qb2 = 0
unc = 0
lit = 0
con = 0
sup = 0
inte = 0
mod = 0

mypath = '/Users/francis/Documents/FORDHAM/2nd Term/Text Analytics/' #path where files are located
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for i in onlyfiles:
	qa = 0
	qb = 0
    if i.endswith('.txt'):
        # get code
        j = i.replace('.txt','')
        # string filename
        file = mypath + str(i)
        f = open(file,'rU')
    	raw = f.read()
    	raw = raw.replace('\n',' ')
    	#raw = raw.decode('utf8')

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

		#version 2 - dictionaries

    	for word in dict_p2:
			if word in raw:
				qa2 += 1

    	for word in dict_n2:
			if word in raw:
				qb2 += 1

    	qc2 = qa2 - qb2

    	if qc2 > 0:
			sentiment2 = 'POSITIVE'
    	elif qc2 == 0:
			sentiment2 = 'NEUTRAL'
    	else:
			sentiment2 = 'NEGATIVE'

		#extended

    	for word in dict_uncertainty:
			if word in raw:
				unc += 1
    	for word in dict_litigious:
			if word in raw:
				lit += 1
    	for word in dict_constraining:
			if word in raw:
				con += 1
    	for word in dict_superfluous:
			if word in raw:
				sup += 1
    	for word in dict_interesting:
			if word in raw:
				inte += 1
    	for word in dict_modal:
			if word in raw:
				mod += 1
		
		
    	rowlist.append(i)
    	rowlist.append(qa)
    	rowlist.append(qb)
    	rowlist.append(qc)
    	rowlist.append(sentiment)
    	rowlist.append(qa2)
    	rowlist.append(qb2)
    	rowlist.append(qc2)
    	rowlist.append(sentiment2)

    	rowlist.append(unc)
    	rowlist.append(lit)
    	rowlist.append(con)
    	rowlist.append(sup)
    	rowlist.append(inte)
    	rowlist.append(mod)

    	print counti
    	counti += 1
    	totallist.append(rowlist)

    	rowlist2 = []
    	rowlist = []


labels = ('file', 'BL_P', 'BL_N', 'BL_NET', 'BL_SENTIMENT','M_P', 'M_N', 'M_NET', 'M_SENTIMENT','M_UNCERTAINTY','M_LITIGIOUS','M_CONSTRAINING','M_SUPERFLUOUS','M_INTERESTING','M_MODAL')
df = pd.DataFrame.from_records(totallist, columns = labels)

df.to_csv('allsentiment.csv', index = False)

	# 	netcnt += qc
	# 	netcnt2 += qc2

	# if netcnt > 0:
	# 	print "V1 - TOTAL +"
	# elif netcnt == 0:
	# 	print "V1 - TOTAL ~"
	# else:
	# 	print "V1 - TOTAL -"
	# netcnt = 0

	# if netcnt2 > 0:
	# 	print "V2 - TOTAL +"
	# elif netcnt2 == 0:
	# 	print "V2 - TOTAL ~"
	# else:
	# 	print "V2 - TOTAL -"
	# netcnt2 = 0