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

