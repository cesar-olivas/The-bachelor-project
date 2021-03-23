import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
stop_words = nltk.corpus.stopwords.words("english")
#NEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWN
myfile = "/Users/Cesar R. Olivas/Desktop/py projects/Bachelorette.txt"  #leave out C:
rtxt = open(myfile).read()
bac_string = str(rtxt) #string text
tokens = nltk.word_tokenize(rtxt) #tokenize

#print(tokens[:6]) #tokenized text
fd = FreqDist(tokens)
#print(fd.most_common(15)) #15 most common tokens
filtered_sentence = [] # no stop words sentence

for w in tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
print("No stop words", filtered_sentence[:15])
fdt = FreqDist(filtered_sentence)
print(fdt.most_common(5)) #5 most common stop-word-free words

from nltk.stem import PorterStemmer     #GETS RID OF DERIVATIONAL AFFIXES

ps = PorterStemmer()
stemmed_words=[]

for w in filtered_sentence:
    stemmed_words.append(ps.stem(w))
print(stemmed_words)

import nltk, re
splits = re.findall(r"\w+(?:[-']\w+)*", str(stemmed_words))
print("\nREGEXP:", splits) #final clean text
clean_fd = FreqDist(splits)
print( "\nclean words", clean_fd.most_common(15)) #most common of clean text