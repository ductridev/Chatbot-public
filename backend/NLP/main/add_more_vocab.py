from gensim.models.word2vec import Word2Vec
import pandas as pd
import numpy as np
import os

root_dir = os.getcwd().replace('\\', '/')
train_data = pd.read_csv(root_dir + '/backend/NLP/data/processed_data4.csv', usecols=[1])
train_data = train_data.values
train_data = np.array(train_data)
train_data = train_data.reshape((1,-1))[0]

pathModelBin=root_dir + '/backend/NLP/models/w2v.bin'
pathModelTxt=root_dir + '/backend/NLP/models/w2v.txt'

model = Word2Vec(train_data, vector_size=150, window=2, min_count=1, sample=0.0001, workers=4, sg=0, negative=10, cbow_mean=1, epochs=50)

model.wv.save_word2vec_format(pathModelBin, fvocab=None, binary=True)
model.wv.save_word2vec_format(pathModelTxt, fvocab=None, binary=False)
print(f"\nTrain done saved to {root_dir}/backend/NLP/model folder.")
