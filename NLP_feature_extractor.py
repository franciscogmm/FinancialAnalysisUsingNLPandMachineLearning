import nltk
from nltk import FreqDist,ngrams
from nltk.corpus import stopwords
import string
from os import listdir
from os.path import isfile, join


def wordfreq(file):
    f = open(file,'rU')
    raw = f.read()
    raw = raw.replace('\n',' ')
    #raw = raw.decode('utf8')
    #tokenization
    tokens = nltk.word_tokenize(raw)
    #stopwords = stopwords.words('english') #use the NLTK stopwords
    #lower everything
    words = [w.lower() for w in tokens] 
    #words_nostop = [w.lower() for w in tokens] 
    #remove numbers
    words = [w for w in words if w.isalpha()]
    #words_nostop = [w for w in words_nostop if w.isalpha()]
    #encode
    words = [w.encode('utf8') for w in words]
    #words_nostop = [w.encode('utf8') for w in words if w not in stopwords]
    #remove punctuations
    words = [w.translate(None, string.punctuation) for w in words]
    #words_nostop = [w.translate(None, string.punctuation) for w in words_nostop]
    freq = FreqDist(words)
    #freq_nostop = FreqDist(words_nostop)
    sorted_freq = sorted(freq.items(),key = lambda k:k[1], reverse = True)
    #sorted_freq_nostop = sorted(freq_nostop.items(),key = lambda k:k[1], reverse = True)
    return sorted_freq

# def sentiment(file):
# 	raw = f.read()
#     raw = raw.replace('\n',' ')
#     #raw = raw.decode('utf8')
#     #tokenization
#     tokens = nltk.word_tokenize(raw)

#     for word in tokens:
    	

def wordfreq(file):
    f = open(file,'rU')
    raw = f.read()
    raw = raw.replace('\n',' ')
    #raw = raw.decode('utf8')
    #tokenization
    tokens = nltk.word_tokenize(raw)
    #stopwords = stopwords.words('english') #use the NLTK stopwords
    #lower everything
    words = [w.lower() for w in tokens] 
    #words_nostop = [w.lower() for w in tokens] 
    #remove numbers
    words = [w for w in words if w.isalpha()]
    #words_nostop = [w for w in words_nostop if w.isalpha()]
    #encode
    words = [w.encode('utf8') for w in words]
    #words_nostop = [w.encode('utf8') for w in words if w not in stopwords]
    #remove punctuations
    words = [w.translate(None, string.punctuation) for w in words]
    #words_nostop = [w.translate(None, string.punctuation) for w in words_nostop]
    freq = FreqDist(words)
    #freq_nostop = FreqDist(words_nostop)
    sorted_freq = sorted(freq.items(),key = lambda k:k[1], reverse = True)
    #sorted_freq_nostop = sorted(freq_nostop.items(),key = lambda k:k[1], reverse = True)
    return sorted_freq

def postag(file,tag):
    f = open(file,'rU')
    raw = f.read()
    print type(raw)
    raw = raw.replace('\n',' ')
    raw = raw.decode("utf-8", 'ignore')

    #tokenization
    tokens = nltk.word_tokenize(raw)
    
    POS_tags = nltk.pos_tag(tokens)
    POS_tags_list = [(word,tag) for (word,tag) in POS_tags if tag.startswith(tag)]
    
    #freq = FreqDist(words)
    #tag_freq = FreqDist(POS_tags_list)
    #sorted_freq = sorted(freq.items(),key = lambda k:k[1], reverse = True)
    #sorted_tag_freq = sorted(tag_freq.items(),key = lambda k:k[1], reverse = True)
    return POS_tags_list

def ngram_list(file,n):
    f = open(file,'rU')
    raw = f.read()
    raw = raw.replace('\n',' ')
    #raw = raw.decode('utf8')
    ngramz = ngrams(raw.split(),n)
    return ngramz

mypath = '/Users/francis/Documents/FORDHAM/2nd Term/Text Analytics/' #path where files are located
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

allwords_nostop = []
allpos_tags = []
allbigrams = []
alltrigrams = []
allfivegrams = []
tag_list = ['N','J','RB','V']
for i in onlyfiles:
    if i.endswith('.txt'):
        # get code
        j = i.replace('.txt','')
        # string filename
        file = mypath + str(i)
        print i
        # allwords_nostop.append(wordfreq_nostop(file))
        # print i + ' ALLWORDS_NOSTOP - OK'
        for tag in tag_list:
        	allpos_tags.append(postag(file,tag))
        	print i + ' POSTAGGING - OK'
        # allbigrams.append(ngram_list(file,2))
        # print i + ' BIGRAM - OK'
        # alltrigrams.append(ngram_list(file,3))
        # print i + ' TRIGRAM - OK'
        # allfivegrams.append(ngram_list(file,5))
        # print i + ' TRIGRAM - OK'
    else:
        pass

AWNS = []
APT = []
BG = []
TG = []
FG = []
# for i in allwords_nostop:
#     AWNS += i
# nostop_freq = FreqDist(AWNS)
# sorted_nostop_freq = sorted(nostop_freq.items(),key = lambda k:k[1], reverse = True)

for i in allpos_tags:
    APT += i
tag_freq = FreqDist(APT)
sorted_tag_freq = sorted(tag_freq.items(),key = lambda k:k[1], reverse = True)

# for i in allbigrams:
#     BG += i
# bg_freq = FreqDist(BG)
# sorted_bg_freq = sorted(bg_freq.items(),key = lambda k:k[1], reverse = True)

# for i in alltrigrams:
#     TG += i
# tg_freq = FreqDist(TG)
#sorted_tg_freq = sorted(tg_freq.items(),key = lambda k:k[1], reverse = True)

# for i in allfivegrams:
#     FG += i
# fg_freq = FreqDist(FG)
# sorted_fg_freq = sorted(fg_freq.items(),key = lambda k:k[1], reverse = True)

# a = 0
# for i in sorted_nostop_freq:
# 	print 'nonstop' +str(a)
#     a+=1
#     with open('sorted_nostop_freq.txt', 'a') as csvfile:
#         csvfile.write(str(i) + '\n')
a = 0
for i in sorted_tag_freq:
	print 'tag' +str(a)
	a+=1
	with open('sorted_tag_extended_freq.txt', 'a') as csvfile:
		csvfile.write(str(i) + '\n')


# a = 0
# for i in sorted_bg_freq:
#     print 'bg' +str(a)
#     a+=1
#     with open('sorted_bg_freq.txt', 'a') as csvfile:
#         csvfile.write(str(i) + '\n')

# a = 0
# for i in sorted_tg_freq:
# 	print 'tg' +str(a)
# 	a+=1
# 	with open('sorted_tg_freq.txt', 'a') as csvfile:
# 		csvfile.write(str(i) + '\n')

# a = 0
# for i in sorted_fg_freq:
# 	print 'fg' +str(a)
# 	a+=1
# 	with open('sorted_fg_freq.txt', 'a') as csvfile:
# 		csvfile.write(str(i) + '\n')