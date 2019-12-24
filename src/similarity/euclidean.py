from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances


def similarity_euclidean(id1, id2):
	cv = CountVectorizer()
	text_lst = []
	text_lst.append(get_text(id1))
	text_lst.append(get_text(id2))
	X=cv.fit_transform(text_lst) #convert text into matrix of word count
	#Normalize the distance between 0 and 1 and substract by 1, so that the closer to 1 the stronger in similarity
	return 1-euclidean_distances(X[0],X[1])/np.max((euclidean_distances(X)))