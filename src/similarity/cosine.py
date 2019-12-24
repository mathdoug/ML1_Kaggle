from sklearn.metrics.pairwise import cosine_similarity


def similarity_cosine(id1, id2):
	text_lst = []
	text_lst.append(get_text(id1))
	text_lst.append(get_text(id2))

	return cosine_similarity(X[0], X[1])