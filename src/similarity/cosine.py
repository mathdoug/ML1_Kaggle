from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

def similarity_cosine(graph, df):
	cs = []

    with open('../../data/training.txt', 'r') as f:
        k =0
        for line in f:
            ans = 0
            line = line.split()
            documentA = get_text(line[0])
            documentB = get_text(line[1])
            vectors = []
            try:
                vectorizer = CountVectorizer()
                vectors = vectorizer.fit_transform([documentA, documentB])
                X = vectors.toarray()
            
                total = np.sum(X, axis = 1) #will be used later to Normalize

                #Handle the case that there is a 0 vector
                if (total[0] == 0) :
                    total[0] += 1
                if(total[1] == 0):
                    total[1] +=1 
            
                #Normalize and calculate the similarity
                X3 = list()
                X3.append(X[0]/ total[0])
                X3.append(X[1]/ total[1])
                sim = cosine_similarity(X3)
                ans = sim[0,1]

            #Handle the case that we compare two empty text or two text with no word, but some symboles 
            except ValueError:
                ans = 0
            cs.append(ans)

    df["Cosine Similarity"] = cs
    return cs