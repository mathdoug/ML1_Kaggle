from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def similarity_cosine(graph, df):
	sim_cosine = []

	cv = CountVectorizer()
	with open('../../data/training.txt', "r") as f:
		for line in f:
			line = line.split()
			text_lst = []
			text_lst.append(get_text(line[0]))
			text_lst.append(get_text(line[1]))
			X=cv.fit_transform(text_lst) #convert text into matrix of word count
			sim_cosine.append(cosine_similarity(X[0], X[1]))
	
	df["Similarity-Cosine"] = sim_cosine
	return