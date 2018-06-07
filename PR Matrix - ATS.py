"""
Given a text document, this code is developed to score the sentences using PageRank. 
This code was developed and used as a part of Automatic Text Summarization Project. 

1. Text document is split into sentences usinf NLTK's Punkt Sentence Tokenizer.
2. A vector of words is created using Counter. Punctuation and stop-words are removed.
3. A matrix where rows as sentences and coulmns as words is created. 
4. TF-IDF transformer is used to normalize the matrix. 
	(re-weighting each word based on tf-idf). 
5. PageRank function from Networkx is used to score the sentences.
	(Score 1 - same sentences, Score 0 - no overlap)
6. Sentences are sorted according to the scores.
7. Most relevant and important sentences are extracted.

"""



# Author: Sai Manasa Nandiwada <saimanasa9@gmail.com>
# Last Modified Date: 05-9-2017
# Created Date: 01-24-2017



from nltk.tokenize.punkt import PunktSentenceTokenizer
from operator import itemgetter
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from collections import Counter
import numpy as np
import networkx as nx



# Open and Read Text Document
	with open("/Users/saimanasanandiwada/Desktop/NLPProject/Sample1.txt", "r") as f1:
		document = f1.read()



# Tokenize Sentences
	document = ' '.join(document.strip().split('\n'))
	sentence_tokenizer = PunktSentenceTokenizer()
	sentences = sentence_tokenizer.tokenize(document)



# Words Collection and Preprocessing
	def bag_of_words(sentence):
		return Counter(word.lower().strip('.,') for word in sentence.split(' '))



# Vector Formation, Matrix Normalization, Graph Conversion, Scoring using PageRank
	def rank(document):
		sentence_tokenizer = PunktSentenceTokenizer()
		sentences = sentence_tokenizer.tokenize(document)
		c = CountVectorizer()
		bow_matrix = c.fit_transform(sentences)
		normalized_matrix = TfidfTransformer().fit_transform(bow_matrix)
		similarity_graph = normalized_matrix * normalized_matrix.T
		nx_graph = nx.from_scipy_sparse_matrix(similarity_graph)
		scores = nx.pagerank(nx_graph)
		sortedss = []
		sortedss = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)
	
		#for i,s in enumerate(sentences):
		#	print s, scores[i]
	
		sortedscores = []
		sortedscores = sorted(sortedss, key=itemgetter(1))
		summaryss = []
		summaryss = sortedscores[:10]
		
		
		
	# print summaryss
	summarysents = []
	summarysents = [x[1] for x in summaryss]
	print summarysents
	
	
	with open("/Users/saimanasanandiwada/Desktop/Summary2.txt", "w") as fout:
		for sents in summarysents:
			print >> fout, sents
	fout.close()
	
	rank(document)
