import os
import pandas as pd
import numpy as np
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

if __name__ == '__main__':
    model = Word2Vec.load('../models/VNCorpus7.bin')
    # fit a 2d PCA model to the vectors
    X = model.wv.vectors
    pca = PCA(n_components=32)
    result = pca.fit_transform(X)

    plt.scatter(result[:, 0], result[:, 1])
    words = list(model.wv.index_to_key)  # Accessing words using index_to_key
    for i, word in enumerate(words):
        plt.annotate(word, xy=(result[i, 0], result[i, 1]))
    plt.show()