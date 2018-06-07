"""
Given a text document, this code lists out the 30 popular sentences of the text document. 
This code was developed and used as a part of Automatic Text Summarization Project. 

1. Text Document is tokenized into Words and Sentences.
2. Each Word is tagged with a POS tag using NLTK.
3. A list of important words is created (POS tag = Noun form).
4. The frequency of each word (from Step 3) is counted.
5. A list of popular words is created from the descending order sorted words based on frequency.
6. First 30 popular words are made into a list.
7. The weight of each sentence is calculated. (Frequency*Rank)
8. Top 30 sentences are sent to the summarizer.


"""
# Author: Sai Manasa Nandiwada <saimanasa9@gmail.com>
# Modified Date: 05-11-2017
# Created Date: 03-15-2017


import nltk
from nltk import word_tokenize, sent_tokenize, pos_tag



# Open and Read Sample Text
	with open("/Users/saimanasanandiwada/Desktop/NLPProject/Sample1.txt", "r") as f1:
		text = f1.read()



# The text is tokenized into words using word_tokenizer. 
# Each token is tagged with parts of speech tag.
	elements = nltk.pos_tag(word_tokenize(text))



# list of important words (pos tag = any noun form) is formed
	wordList = []
	for word, tag in elements:
		if any (c in tag for c in ('NN', 'NNP', 'NNS')):
			wordList.append(word)



# Occurence of each word in the text is counted and a list of popular words is created.
	word_counter = {}
		for word in wordList:
			if word in word_counter:
				word_counter[word] += 1
   			else:
   				word_counter[word] = 1



# Sorted Popular Words
	popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
	top_30 = popular_words[:30]
		#print top_30


# Weight Calculation of Sentences 
sent_counter = {}
sentences = sent_tokenize(text)
for sents in sentences:
	if word in top_30:
		sent_counter[sents] += 1
	else:
		sent_counter[sents] = 0



# Sorted Popular Sentences
popular_sentences = sorted(sent_counter, key = sent_counter.get, reverse = True)
top_30sents = popular_sentences[:30]
#print top_30sents



with open("/Users/saimanasanandiwada/Desktop/NLPProject/Summary1.txt", "w") as fout:
	for sent in top_30sents:
		print >> fout, sent
fout.close()







