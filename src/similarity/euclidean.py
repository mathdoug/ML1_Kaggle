from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances


def similarity_euclidean(graph, df):
	sim_eu = []

	cv = CountVectorizer()
	with open('../../data/training.txt', "r") as f:
		for line in f:
			line = line.split()
			text_lst = []
			text_lst.append(get_text(line[0]))
			text_lst.append(get_text(line[1]))
			X=cv.fit_transform(text_lst) #convert text into matrix of word count
			#Normalize the distance between 0 and 1 and substract by 1, so that the closer to 1 
			#the stronger in similarity
			sim_eu.append(1-euclidean_distances(X[0],X[1])/np.max((euclidean_distances(X))))
	
	df["Similarity-Euclidean"] = sim_eu
	return