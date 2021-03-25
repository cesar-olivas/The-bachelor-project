# The-bachelorette-project
**The Bachelorette Project** 

How do contestants on a dating reality tv show convey legitimacy and intentionality? How do the words they painstakingly choose reflect their deeply-held beliefs about romance, destiny and love? These are the guiding questions for the current project which takes transcripts from _season 14_ of **The Bachelorette** and **NLTK** libraries and programs to mine the data.  The goal is to study the language of male contestants for  linguistic patterns that will provide insight into the semantic and conceptual underpinnings of common themes such as _gender, love, fear, partnership, sincerity_ and other commonly held views of relationships. Eventually I hope to do the same with seasons of **The Bachelor** (all female contestants) and compare and contrast the differences in gendered language.

**The Transcripts**\
With the success of the long running program, transcripts of the show are made available to the public through online directories. The transcripts for the entire season were pulled from <https://transcripts.foreverdreaming.org/viewforum.php?f=292> and copied on to a .txt file for mining. This allowed me to accurately control text boundaries and made cleaning the data a tiny bit easier. 

**Bach-test.py**\
This is the initial entry of the project. The .txt file is accessed and read by the program, converted to _strings_, then _tokenized_, and then sequenced into _bigrams_. To find word collocation, the _bigrams_ are then iterated through a _next_words_ variable which will return every second element where the first element matches the condition **"love"**. Following this is a for loop to find the next possible words for any of interest in the data based on the first 8,000 words in the database. Of interest here is the use of "so" as a modifier likely preceding the adjective "wrong".

**cleaning-data.py**\
This second focuses on cleaning the data, removing stop words, punctuation, etc... First the .txt file is accessed and read, and a _stop_words_ is introduced. Then I made a _filtered_sentence_ variable with an empty list which is "appended" by a for loop which iterated through the data to extract all the words that are not in the _stop_words_ variable. This rids the data of high frequency non-content words such as _"the, a, an, etc..."_. Then a _PorterStemmer_ module is imported to get rid of all derivational affixes and leave only root words. Words are stripped down of morphological variants and reduced to base form for example _"likes->like"_, thus making it easier to categorize and count. Finally I use a _REGEXP_ to get rid of dashes, and punctuation in words. While data can always be cleaner, this was a suitable place for me to start digging through the language.

**Word-parsing.py**\
While maintaining the previous variables and imported modules, this portion of the project begins to tease apart and categorize the language. A _POS-tagger_ is introduced to attach a _part of speech tag_ to each word, thereby identifying nouns, verbs, adjectives, etc... Each part of speech variable is given a list comprehension value to indicate the specific _pos tag_ to be returned. A _frequency_ variable is incorporated to construct a frequency distribution count. Then a print function returns the top 15 most common words and the number of times it appears for each part of speech. While the tagging is not fine tuned, the code returns a list of entries which are easy to differentiate. The final portion looks at the word environment by returning all examples of explicit words using _concordance_. This allows for better insight into the semantic nature of the words in question.

**Project Goals**\
As an introductory step into large data minning this project is in its infancy. I would like to learn how to further clean my data, better train to _POS-tagger_, and write more elegant code. My long term goal is to be able to perform _sentiment analysis_ on the data, as my attempts so far have been unsucessful. Additionally I would like to be able to present my findings through graphical representation and chart visualization to make results easy to follow.  

**Contributing**\
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

**References**\
https://transcripts.foreverdreaming.org/viewforum.php?f=292 \
https://www.makeareadme.com/ \
https://www.nltk.org/book/ \
https://www.analyticsvidhya.com/blog/2020/07/part-of-speechpos-tagging-dependency-parsing-and-constituency-parsing-in-nlp \
https://pythonprogramming.net/part-of-speech-tagging-nltk-tutorial/ \
https://stackoverflow.com/questions/29110950/python-concordance-command-in-nltk/43880265

