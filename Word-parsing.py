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
#print("No stop words", filtered_sentence[:15])
fdt = FreqDist(filtered_sentence)
#print(fdt.most_common(5)) #5 most common stop-word-free words

from nltk.stem import PorterStemmer     #GETS RID OF DERIVATIONAL AFFIXES

ps = PorterStemmer()
stemmed_words=[]

for w in filtered_sentence:
    stemmed_words.append(ps.stem(w))
#print(stemmed_words)

import nltk, re
splits = re.findall(r"\w+(?:[-']\w+)*", str(stemmed_words))
#print("\nREGEXP:", splits) #final clean text
clean_fd = FreqDist(splits)
#print( "\nclean words", clean_fd.most_common(15)) #most common of clean text

#Not all the way cleaned and tagged correctly but still provides good insight
tagged_tokens = nltk.pos_tag(splits)
print("\nPOS tagged tokens", tagged_tokens) #POS TAGGING!!!!
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

cfd = nltk.ConditionalFreqDist((target, fileid[:4])

#NOUN PHRASE CHUNKING
#sentence = tagged_tokens[:12]
#grammar = "NP: {<DT>?<JJ>*<NN>}"

#cp = nltk.RegexpParser(grammar)
#result = cp.parse(sentence)
#print(result)
