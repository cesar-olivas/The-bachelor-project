import nltk
from pathlib import Path
from nltk import FreqDist
import nltk
import random
from nltk.corpus import stopwords
stopwords = nltk.corpus.stopwords.words("english")
#NEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWN
#Txt file of show transcripts  (Seasonn 14) sourced from:
#https://transcripts.foreverdreaming.org/viewforum.php?f=292
myfile = "/Users/Cesar R. Olivas/Desktop/py projects/Bachelorette.txt"  # Mac users should leave out C:
rtxt = open(myfile).read() #read txt file
bac_string = str(rtxt) # convert to string text
tokens = nltk.word_tokenize(rtxt) #tokenize

words = random.choice(tokens)
print("random word:", words)

bigram = nltk.bigrams(tokens) #create bigrams
cfd = nltk.ConditionalFreqDist(bigram)

word = random.choice(tokens)
print("random word:", word)

# generate 15 more words
#for i in range(15):
 #   print(word),
  #  if word in cfd:
   #     word = random.choice(cfd[word].keys())
    #else:
     #   break


words = tokens[:400]
print(words)
#To create bigrams, we will iterate through the list of the words with two indices,
# one of which is offset by one:
bigrams = [b for b in zip(words[:-1], words[1:])]
print(bigrams)
#Return every second element where the first element matches the condition:
condition = 'love'
next_words = [bigram[1] for bigram in bigrams
          if bigram[0].lower() == condition]
print("next words:", next_words)
#We have now found all of the possible words that can follow the condition “the” according to our corpus:

#in order to predict the next word, what we really want to compute is what
# is the most likely next word out of all of the possible next words.

from collections import defaultdict
cfd = defaultdict(lambda: defaultdict(lambda: 0))
for i in range(len(words) - 2):  # loop to the next-to-last word
    cfd[words[i].lower()][words[i+1].lower()] += 1

# pretty print the defaultdict
print({k: dict(v) for k, v in dict(cfd).items()})

#So, what’s the most likely word to follow 'the'?
print("next likely word: ", max(cfd['the']))

#https://www.hallada.net/2017/07/11/generating-random-poems-with-python.html

import nltk
from nltk.corpus import stopwords
stop_words = nltk.corpus.stopwords.words("english")
#NEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWN
myfile = "/Users/Cesar R. Olivas/Desktop/py projects/Bachelorette.txt"  # Mac users should leave out C:
rtxt = open(myfile).read()
bac_string = str(rtxt) #string text
tokens = nltk.word_tokenize(rtxt)



print(tokens[:6]) #tokenized text
fd = FreqDist(tokens)
print(fd.most_common(15)) #15 most common tokens
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

#Not all the way cleaned and tagged correctly but still provides good insight
tagged_tokens = nltk.pos_tag(splits)
print(tagged_tokens) #POS TAGGING!!!!
nouns_and_verbs = [token[0] for token in tagged_tokens if token[1] in ['VBD', 'VBP', 'NN', "NNP", "NNS"]]
frequency = nltk.FreqDist(nouns_and_verbs)
print("\nNoun and Verb Freq", frequency.most_common(15)) #PRINTS WORD AND NUMBER OF OCCURANCE BUT NO TAG
adjectives = [token[0] for token in tagged_tokens if token[1] in ['JJ', 'JJR', 'JJS']]
frequency_j = nltk.FreqDist(adjectives)
print("Adjectives Freq", frequency_j.most_common(15)) #adjective most common
verbs_1 = [token[0] for token in tagged_tokens if token[1] in ['VB', 'VBD',"VBZ"]] #'VBG', "VBN", "VBP", THESE THINGS RENDER A MUSCH
# MORE DIFFICULT GROUP OF VERBS TO INTERPRET
frequency_v = nltk.FreqDist(verbs_1)
print("Verbs Freq", frequency_v.most_common(15)) #adjective most common
nouns_1 = [token[0] for token in tagged_tokens if token[1] in ['NN', "NNS"]] #'NNPS',"NNS","NNP"
frequency_n = nltk.FreqDist(nouns_1)
print("Nouns Freq", frequency.most_common(20)) #PRINTS WORD AND NUMBER OF OCCURANCE BUT NO TAG

#Word condordance, better insight into lingusitic environment
import nltk.corpus
from nltk.text import Text
moby = Text(nltk.corpus.gutenberg.words('/Users/Cesar R. Olivas/Desktop/py projects/Bachelorette.txt'))
print("\n LOVE CONCOR", moby.concordance("know"))
print("\n MAN CONCOR", moby.concordance("honest"))
print("\n MAN CONCOR", moby.concordance("real"))

#NOUN PHRASE CHUNKING
#sentence = tagged_tokens[:12]
#grammar = "NP: {<DT>?<JJ>*<NN>}"

#cp = nltk.RegexpParser(grammar)
#result = cp.parse(sentence)
#print(result)




